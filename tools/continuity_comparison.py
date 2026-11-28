
#!/usr/bin/env python3
"""Public reference controls. Not VRP; no native implementation claims."""

import argparse
import csv
import hashlib
import json
import secrets
import socket
import time
from pathlib import Path

HOST = '127.0.0.1'

FIELDS = [
    'model',
    'round',
    'client_port',
    'endpoint_changed',
    'delivery',
    'same_lifetime',
    'sequence_preserved',
    'continuation',
    'elapsed_ns'
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def encode(value):
    return json.dumps(
        value,
        separators=(',', ':')
    ).encode() + b'\n'


def read_line(sock):
    data = bytearray()

    while not data.endswith(b'\n'):
        chunk = sock.recv(1)

        require(bool(chunk), 'unexpected EOF')

        data.extend(chunk)

        require(
            len(data) <= 4096,
            'message too large'
        )

    return json.loads(data)


def reference_state():
    return {
        'lifetime': secrets.token_hex(16),
        'sequence': 0
    }


def response(state, request):
    state['sequence'] += 1

    return {
        'label': request['label'],
        'nonce': request['nonce'],
        **state
    }


def observe(initial, previous, current, expected_nonce):
    delivery = (
        current['nonce'] == expected_nonce
        and current['label'] == initial['label']
    )

    same = (
        current['lifetime'] == initial['lifetime']
    )

    sequence = (
        current['sequence'] ==
        previous['sequence'] + 1
    )

    return (
        delivery,
        same,
        sequence,
        delivery and same and sequence
    )


def run_model(model, rounds, interval):
    tcp = model != 'udp_endpoint_bound'

    kind = (
        socket.SOCK_STREAM
        if tcp else socket.SOCK_DGRAM
    )

    persistent = reference_state()

    rows = []

    # Keep local port reservations alive to
    # prevent accidental port reuse.

    clients = []

    try:
        with socket.socket(
            socket.AF_INET,
            kind
        ) as server:

            server.settimeout(3)
            server.bind((HOST, 0))

            if tcp:
                server.listen(1)

            start = time.monotonic()

            initial = previous = None
            previous_port = None

            for i in range(rounds + 1):

                delay = (
                    start + i * interval
                    - time.monotonic()
                )

                if delay > 0:
                    time.sleep(delay)

                t0 = time.monotonic_ns()

                client = socket.socket(
                    socket.AF_INET,
                    kind
                )

                clients.append(client)

                client.settimeout(3)
                client.bind((HOST, 0))
                client.connect(server.getsockname())

                port = client.getsockname()[1]

                request = {
                    'label': 'public-reference-session',
                    'nonce': secrets.token_hex(16)
                }

                state = (
                    persistent
                    if model == 'tcp_independent'
                    else reference_state()
                )

                client.sendall(encode(request))

                if tcp:
                    peer, addr = server.accept()

                    with peer:
                        peer.settimeout(3)

                        received = read_line(peer)

                        require(
                            received == request,
                            'request mismatch'
                        )

                        require(
                            addr[1] == port,
                            'peer port mismatch'
                        )

                        peer.sendall(
                            encode(
                                response(state, received)
                            )
                        )

                    current = read_line(client)

                    require(
                        client.recv(1) == b'',
                        'expected connection EOF'
                    )

                    client.shutdown(socket.SHUT_WR)

                else:
                    raw, addr = server.recvfrom(4096)

                    received = json.loads(raw)

                    require(
                        received == request,
                        'request mismatch'
                    )

                    require(
                        addr[1] == port,
                        'peer port mismatch'
                    )

                    server.sendto(
                        encode(
                            response(state, received)
                        ),
                        addr
                    )

                    current = json.loads(
                        client.recv(4096)
                    )

                if initial is None:
                    initial = current.copy()

                    require(
                        current['nonce'] == request['nonce']
                        and current['label'] == request['label']
                        and current['sequence'] == 1,
                        'invalid baseline'
                    )

                    values = (
                        True,
                        None,
                        None,
                        None
                    )

                else:
                    values = observe(
                        initial,
                        previous,
                        current,
                        request['nonce']
                    )

                changed = (
                    None
                    if previous_port is None
                    else port != previous_port
                )

                rows.append(
                    dict(zip(
                        FIELDS,
                        [
                            model,
                            i,
                            port,
                            changed,
                            *values,
                            time.monotonic_ns() - t0
                        ]
                    ))
                )

                previous = current.copy()
                previous_port = port

    finally:
        for client in clients:
            client.close()

    return rows


def controls():
    initial = {
        'label': 'same-label',
        'lifetime': 'original',
        'sequence': 1,
        'nonce': 'a'
    }

    valid = dict(
        initial,
        sequence=2,
        nonce='b'
    )

    cases = {
        'valid_continuation': observe(
            initial,
            initial,
            valid,
            'b'
        )[3],

        'replacement_same_label_rejected': not observe(
            initial,
            initial,
            dict(valid, lifetime='replacement'),
            'b'
        )[3],

        'sequence_reset_rejected': not observe(
            initial,
            initial,
            dict(valid, sequence=1),
            'b'
        )[3],

        'wrong_response_rejected': not observe(
            initial,
            initial,
            dict(valid, nonce='wrong'),
            'b'
        )[3]
    }

    return cases


def digest(data):
    return hashlib.sha256(data).hexdigest()


def verify_package(out, expected_manifest_digest):
    manifest = (
        out / 'SHA256SUMS'
    ).read_bytes()

    require(
        digest(manifest) == expected_manifest_digest,
        'manifest commitment mismatch'
    )

    expected = {
        'MEASUREMENTS.csv',
        'VERIFICATION_RESULTS.json'
    }

    seen = set()

    for line in manifest.decode('ascii').splitlines():

        value, sep, name = line.partition('  ')

        require(
            sep
            and name in expected
            and name not in seen,
            'invalid manifest entry'
        )

        path = out / name

        require(
            not path.is_symlink()
            and path.is_file(),
            'invalid artifact type'
        )

        require(
            digest(path.read_bytes()) == value,
            'artifact digest mismatch'
        )

        seen.add(name)

    require(
        seen == expected,
        'missing artifact'
    )


def main():
    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        '--rounds',
        type=int,
        default=30
    )

    parser.add_argument(
        '--interval',
        type=float,
        default=2.0
    )

    parser.add_argument(
        '--out',
        type=Path,
        required=True
    )

    args = parser.parse_args()

    require(
        1 <= args.rounds <= 100,
        'rounds must be 1..100'
    )

    require(
        0 <= args.interval <= 60,
        'interval must be 0..60 seconds'
    )

    args.out.mkdir(
        mode=0o700,
        parents=False,
        exist_ok=False
    )

    rows = []
    summaries = {}

    for model in (
        'tcp_connection_bound',
        'udp_endpoint_bound',
        'tcp_independent'
    ):

        records = run_model(
            model,
            args.rounds,
            args.interval
        )

        rows.extend(records)

        transitions = records[1:]

        expected = (
            args.rounds
            if model == 'tcp_independent'
            else 0
        )

        continued = sum(
            r['continuation'] is True
            for r in transitions
        )

        changed = sum(
            r['endpoint_changed'] is True
            for r in transitions
        )

        delivered = sum(
            r['delivery'] is True
            for r in records
        )

        summaries[model] = {
            'delivery': delivered,
            'observed_port_changes': changed,
            'continuations': continued,
            'expected_continuations': expected,
            'pass': (
                delivered == args.rounds + 1
                and changed == args.rounds
                and continued == expected
            )
        }

    negative = controls()

    passed = (
        all(
            x['pass']
            for x in summaries.values()
        )
        and all(negative.values())
    )

    with (
        args.out / 'MEASUREMENTS.csv'
    ).open(
        'x',
        newline='',
        encoding='utf-8'
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=FIELDS
        )

        writer.writeheader()
        writer.writerows(rows)

    result = {
        'schema_version': '1.0',
        'evaluation_mode': 'PUBLIC_REFERENCE_MODEL',
        'rounds_per_model': args.rounds,
        'scheduled_interval_seconds': args.interval,
        'models': summaries,
        'observer_controls': negative,
        'overall_status': (
            'PASS' if passed else 'FAIL'
        ),
        'native_vrp': 'NOT_TESTED',
        'quic': 'NOT_TESTED',
        'mptcp': 'NOT_TESTED',
        'authority_integrity': 'NOT_TESTED',
        'limitations': [
            'Loopback only',
            'Same-process reference observer',
            'UDP client ports retained until workload ends',
            'TCP connections deliberately terminated',
            'No native VRP identity oracle',
            'No NAT or fault injection',
            'No independent provenance authentication'
        ]
    }

    (
        args.out / 'VERIFICATION_RESULTS.json'
    ).write_text(
        json.dumps(result, indent=2) + '\n',
        encoding='utf-8'
    )

    manifest = ''.join(
        digest(
            (args.out / name).read_bytes()
        ) + '  ' + name + '\n'
        for name in (
            'MEASUREMENTS.csv',
            'VERIFICATION_RESULTS.json'
        )
    )

    (
        args.out / 'SHA256SUMS'
    ).write_text(
        manifest,
        encoding='ascii'
    )

    commitment = digest(
        manifest.encode('ascii')
    )

    verify_package(
        args.out,
        commitment
    )

    print(json.dumps(result, indent=2))

    print(
        'MANIFEST_SHA256=' + commitment
    )

    print('LOCAL_INTEGRITY=PASS')

    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())

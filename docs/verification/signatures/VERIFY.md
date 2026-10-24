# VRP Public Manifest Signature Verification

This directory contains public verification material for a signed
Veil Routing Protocol documentation integrity manifest.

## Signer

Identity:

    vitalijus-riabovas-vrp

Signature algorithm:

    Ed25519

Signature format:

    OpenSSH SSHSIG

Signature namespace:

    vrp-evidence

Expected public-key fingerprint:

    SHA256:xeyh/yOOAoP41r/D+bHabhMjPaMqRb2dcI1rteShzgQ

## Files

    vrp-manifest-signing-key.pub
    allowed_signers
    VRP-DOCUMENTATION-SHA256-20261024T173934Z.txt
    VRP-DOCUMENTATION-SHA256-20261024T173934Z.txt.sig

The private signing key is not part of this repository.

## Verify the public-key fingerprint

Run:

    ssh-keygen -lf vrp-manifest-signing-key.pub -E sha256

Expected fingerprint:

    SHA256:xeyh/yOOAoP41r/D+bHabhMjPaMqRb2dcI1rteShzgQ

## Verify the manifest SHA-256

Run:

    sha256sum VRP-DOCUMENTATION-SHA256-20261024T173934Z.txt

Expected SHA-256:

    8c2dc03d5152c0b8a880bb5e424e5a06f217d7b50f3279bc17af802a8c9e151e

## Verify the Ed25519 signature

Run from this directory:

    ssh-keygen -Y verify \
      -f allowed_signers \
      -I vitalijus-riabovas-vrp \
      -n vrp-evidence \
      -s VRP-DOCUMENTATION-SHA256-20261024T173934Z.txt.sig \
      < VRP-DOCUMENTATION-SHA256-20261024T173934Z.txt

A successful verification should report a good `vrp-evidence`
signature for `vitalijus-riabovas-vrp`.

## Security boundary

The files in this directory are public verification material only.

The private signing key and any signing-key passphrase must never be
committed, published, copied into this directory, or distributed.

The signature proves that the manifest was signed by the private key
corresponding to the published Ed25519 public key.

The identity associated with that key depends on the provenance and
trust established for the published public key and fingerprint.

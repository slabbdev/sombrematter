"""Ed25519 — RFC 8032 reference implementation, Python stdlib only.

Vendored for SombreMatter's seal so the creature's life-signatures need no
dependencies on the runner. This is the reference construction from
RFC 8032 / the original djb reference port (public domain): scalar
arithmetic on the twisted Edwards curve birationally equivalent to
Curve25519. Slow in pure Python (~0.1 s per operation) — fine for one
signature per heartbeat.

Self-test: python3 sleep/ed25519.py  (RFC 8032 test vector 1)
"""

import hashlib

b = 256
q = 2 ** 255 - 19
l = 2 ** 252 + 27742317777372353535851937790883648493


def H(m):
    return hashlib.sha512(m).digest()


def inv(x):
    return pow(x, q - 2, q)


d = (-121665 * inv(121666)) % q
I = pow(2, (q - 1) // 4, q)


def xrecover(y):
    xx = (y * y - 1) * inv(d * y * y + 1)
    x = pow(xx, (q + 3) // 8, q)
    if (x * x - xx) % q != 0:
        x = (x * I) % q
    if x % 2 != 0:
        x = q - x
    return x


By = (4 * inv(5)) % q
B = [xrecover(By), By]


def edwards(P, Q):
    x1, y1 = P
    x2, y2 = Q
    x3 = (x1 * y2 + x2 * y1) * inv(1 + d * x1 * x2 * y1 * y2)
    y3 = (y1 * y2 + x1 * x2) * inv(1 - d * x1 * x2 * y1 * y2)
    return [x3 % q, y3 % q]


def scalarmult(P, e):
    Q = [0, 1]
    while e:
        if e & 1:
            Q = edwards(Q, P)
        P = edwards(P, P)
        e >>= 1
    return Q


def encodepoint(P):
    x, y = P
    data = bytearray(y.to_bytes(32, "little"))
    if x & 1:
        data[31] |= 0x80
    return bytes(data)


def isoncurve(P):
    x, y = P
    return (-x * x + y * y - 1 - d * x * x * y * y) % q == 0


def decodepoint(s):
    y = int.from_bytes(s, "little") & ((1 << 255) - 1)
    x = xrecover(y)
    if x & 1 != (s[31] >> 7) & 1:
        x = q - x
    P = [x, y]
    if not isoncurve(P):
        raise ValueError("decoding point that is not on curve")
    return P


def secret_expand(sk):
    h = H(sk)
    a = int.from_bytes(h[:32], "little")
    a &= (1 << 254) - 8
    a |= (1 << 254)
    return a, h[32:]


def publickey(sk):
    a, _ = secret_expand(sk)
    return encodepoint(scalarmult(B, a))


def sign(m, sk, pk):
    a, prefix = secret_expand(sk)
    r = int.from_bytes(H(prefix + m), "little") % l
    R = encodepoint(scalarmult(B, r))
    k = int.from_bytes(H(R + pk + m), "little") % l
    s = (r + k * a) % l
    return R + s.to_bytes(32, "little")


def valid(sig, m, pk):
    if len(sig) != 64 or len(pk) != 32:
        return False
    try:
        A = decodepoint(pk)
        R = sig[:32]
        S = int.from_bytes(sig[32:], "little")
        if S >= l:
            return False
        k = int.from_bytes(H(R + pk + m), "little") % l
        lhs = scalarmult(B, S)
        rhs = edwards(decodepoint(R), scalarmult(A, k))
        return encodepoint(lhs) == encodepoint(rhs)
    except (ValueError, IndexError):
        return False


if __name__ == "__main__":
    # RFC 8032 test-vector-1 seed; signature cross-checked byte-for-byte
    # against OpenSSL 3 (pkeyutl, Ed25519) on message "abc".
    seed = bytes.fromhex(
        "9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60")
    want_pub = "d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a"
    want_sig = ("80d724b01e7ca260f4cc7f8de7c95f73cfac615bab1f762b6435b6ec26c8cf6"
                "d2c758dae2f87399a8eeda1cbcd2835ac5ba66d6ecaa3aba5e567a751053dc207")
    pk = publickey(seed)
    sg = sign(b"abc", seed, pk)
    assert pk.hex() == want_pub, "public key mismatch"
    assert sg.hex() == want_sig, "signature mismatch"
    assert valid(sg, b"abc", pk), "valid signature rejected"
    assert not valid(sg, b"tampered", pk), "tampered message accepted"
    print("ed25519: self-test vs OpenSSL-verified vectors — OK")

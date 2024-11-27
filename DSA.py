 Algorithm:
 Key Generation:
o Private Key: This key is kept secret by the owner
and is used to create the digital signature.
o Public Key: This key is made available to everyone
and is used to verify the authenticity of the
signature.
o The DSA key generation involves choosing prime
numbers p and q and generating a base g.
o The private key x is selected randomly, and the
corresponding public key y is computed using
modular exponentiation.
 Signing Process: To sign a message M, the
following steps are taken:
o A hash of the message (H(M)) is calculated using
a hash function (e.g., SHA-2).
o A random number k is selected (for security, k
must be different for each signature).
o Two values, r and s, are computed using modular
arithmetic.
r = (g^k mod p) mod q
s = k^(-1) * (H(M) + x * r) mod q
o The signature consists of the pair (r, s).
 Verification Process: To verify the signature (r, s)
on the message M:
o The verifier computes the hash H(M) of the
message.
o The public key y is used to verify the signature
using the formula:
v = (g^H(M) mod p) mod q
o If v == r, the signature is valid, indicating that
the message has not been tampered with and is
from the claimed sender.


import hashlib
import random
from sympy import mod_inverse

# Generate a prime number (p) and a base (g)
# In practice, p and g are usually very large prime numbers. Here, we use smaller primes for simplicity.
p = 7919  # A small prime number
q = 997   # Another small prime number
g = 5     # A generator for the group

# Private Key (x) is a random integer less than q
private_key = random.randint(1, q - 1)

# Public Key (y) is g^x mod p
public_key = pow(g, private_key, p)

# Hash function (SHA-256)
def hash_message(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)

# Generate a Digital Signature
def sign(message, private_key):
    # Hash the message
    h = hash_message(message)

    # Calculate the value of k (random integer less than q)
    k = random.randint(1, q - 1)

    # Calculate r = (g^k mod p) mod q
    r = pow(g, k, p) % q

    # Calculate s = k^(-1) * (h + x * r) mod q
    k_inv = mod_inverse(k, q)
    s = (k_inv * (h + private_key * r)) % q

    return r, s

# Verify a Digital Signature
def verify(message, r, s, public_key):
    # Hash the message
    h = hash_message(message)

    # Check if r and s are in valid ranges
    if r <= 0 or r >= q or s <= 0 or s >= q:
        return False

    # Calculate w = s^(-1) mod q
    w = mod_inverse(s, q)

    # Calculate u1 = h * w mod q
    u1 = (h * w) % q

    # Calculate u2 = r * w mod q
    u2 = (r * w) % q

    # Calculate v = (g^u1 * y^u2 mod p) mod q
    v = (pow(g, u1, p) * pow(public_key, u2, p)) % p % q

    # The signature is valid if v == r
    return v == r


# User input
message = input("Enter the message to be signed: ")

# Generate the signature for the message
r, s = sign(message, private_key)

# Verify the signature
is_valid = verify(message, r, s, public_key)

# Display results
print(f"Message: {message}")
print(f"Signature (r, s): ({r}, {s})")
print(f"Public Key: {public_key}")
print(f"Signature valid: {is_valid}")

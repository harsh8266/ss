Algorithm:
1. Choose Public Parameters:
Both parties agree on a large prime number p and a base g
(also called the generator), where g < p.
2. Generate Private Keys:
Each party selects a private key (a random integer) a and b,
kept secret from each other.
3. Compute Public Keys:
Each party computes their public key:
Party A computes A= g^a mod p
Party B computes B= g^b mod p
They then exchange these public keys over the insecure
channel.
4. Compute the Shared Secret:
Each party then computes the shared secret using the other’s
public key and their own private key:
Party A computes s = B^a mod p
Party B computes s = A^b mod p
5. Both will arrive at the same shared secret s, which
can be used for further encryption.


# Diffie-Hellman Code

# Power function to return value of a^b mod P
def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

# Main function
def main():
    # Both persons agree upon the public keys G and P
    # A prime number P is taken
    P = 23
    print("The value of P:", P)

    # A primitive root for P, G is taken
    G = 9
    print("The value of G:", G)

    # Alice chooses the private key a
    # a is the chosen private key
    a = 4
    print("The private key a for Alice:", a)

    # Gets the generated key
    x = power(G, a, P)

    # Bob chooses the private key b
    # b is the chosen private key
    b = 3
    print("The private key b for Bob:", b)

    # Gets the generated key
    y = power(G, b, P)

    # Generating the secret key after the exchange of keys
    ka = power(y, a, P)  # Secret key for Alice
    kb = power(x, b, P)  # Secret key for Bob

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)

if __name__ == "__main__":
    main()

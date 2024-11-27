Algorithm:
 Key Generation:
o Choose two large prime numbers, p and q.
o Compute n = p × q. This is the modulus for the keys.
o Compute the totient ϕ(n)=(p − 1) × (q − 1).
o Choose a public exponent e such that 1 < e < ϕ(n) and
gcd(e,ϕ(n))=1.
o Compute the private key d such that e×d≡1 (mod ϕ(n)).
Public Key: (e,n).
Private Key: (d,n).
 Signing a Message:
o Hash the message M using a secure hash function
(e.g., SHA-256).
o Convert the hash H(M) into an integer representation
m.
o Compute the digital signature S using the private
key:
S = m^d mod n
 Verifying a Signature:
o Given the signature S and the original message M,
hash the message M to obtain H(M).
o Convert H(M) into an integer representation m.
o Use the public key to compute:
m’ = S^e mod n
o If m′ equals m (the hash of the original message), the
signature is valid.

# Function to find gcd 
# of two numbers
def euclid(m, n):
	
	if n == 0:
		return m
	else:
		r = m % n
		return euclid(n, r)
	
	
# Program to find 
# Multiplicative inverse
def exteuclid(a, b):
	
	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)
	
	while r2 > 0:
		
		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t
		
	if t1 < 0:
		t1 = t1 % a
		
	return (r1, t1)

# Enter two large prime
# numbers p and q
p = 823
q = 953
n = p * q
Pn = (p-1)*(q-1)

# Generate encryption key 
# in range 1<e<Pn
key = []

for i in range(2, Pn):
	
	gcd = euclid(Pn, i)
	
	if gcd == 1:
		key.append(i)


# Select an encryption key 
# from the above list
e = int(313)

# Obtain inverse of 
# encryption key in Z_Pn
r, d = exteuclid(Pn, e)
if r == 1:
	d = int(d)
	print("decryption key is: ", d)
	
else:
	print("Multiplicative inverse for\
	the given encryption key does not \
	exist. Choose a different encryption key ")


# Enter the message to be sent
M = 19070

# Signature is created by Alice
S = (M**d) % n

# Alice sends M and S both to Bob
# Bob generates message M1 using the
# signature S, Alice's public key e 
# and product n.
M1 = (S**e) % n

# If M = M1 only then Bob accepts
# the message sent by Alice.

if M == M1:
	print("As M = M1, Accept the\
	message sent by Alice")
else:
	print("As M not equal to M1,\
	Do not accept the message\
	sent by Alice ")

Algorithm:
 Input Preparation:
Accept an input string to be hashed (e.g., "WHO GOES
THERE?").
 Initialization:
Import the hashlib library, which contains the built-in
SHA-1 hashing function.
Create a SHA-1 hash object using hashlib.sha1().
 Data Encoding:
Convert the input string to byte format using the
encode() method (e.g., UTF-8 encoding).
 Hashing Process:
Feed the byte-encoded data into the SHA-1 hash object
using the update() method.
 Result Extraction:
Use the hexdigest() method to retrieve the final SHA-1
hash as a hexadecimal string.
 Output:
Print or return the SHA-1 hash value


import hashlib

def sha1(message):
   # generate a SHA-1 hash object
   sha1_hash = hashlib.sha1()

   # update the hash object 
   sha1_hash.update(message.encode('utf-8'))

   # hexadecimal digest of the hash
   return sha1_hash.hexdigest()

# execute the function
message = "Hello, everyone!"
sha1_hash = sha1(message)
print("SHA-1 hash:", sha1_hash)

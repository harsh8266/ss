Algorithm:
 Input Preparation:
Accept a string input that needs to be hashed.
 Initialization:
Import the hashlib library to use its built-in MD5 hashing
function.
Create an MD5 hash object using hashlib.md5().
 Data Encoding:
Encode the input string to bytes using UTF-8 encoding
(since hashlib requires byte data for the hashing process).
 Hashing Process:
Use the update() method to feed the encoded data into the
MD5 hash object.
 Result Extraction:
Call the hexdigest() method to get the final hexadecimal
representation of the MD5 hash.
 Output:
Print or return the MD5 hash.

# importing the required libraries
import hashlib
# making a message
inputstring = "This is a message sent by a computer user."
# encoding the message using the library function
output = hashlib.md5(inputstring.encode())
# printing the hash function
print("Hash of the input string:")
print(output.hexdigest())

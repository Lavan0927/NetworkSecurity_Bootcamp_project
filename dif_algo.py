#Write a program in python to generate hashes in string data using 3 algorithm from hashlib library

import hashlib
mystring = input('Enter string to hash: ')
hash1_obj = hashlib.md5(mystring.encode())
hash2_obj = hashlib.sha384(mystring.encode())
hash3_obj = hashlib.blake2b(mystring.encode())
print(hash1_obj.hexdigest())
print(hash2_obj.hexdigest())
print(hash3_obj.hexdigest())

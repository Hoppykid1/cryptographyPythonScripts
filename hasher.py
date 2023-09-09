import hashlib

print("Options: ")
print(hashlib.algorithms_guaranteed)

hash_it = input("Please enter something to be hashed: ")
hashed = hashlib.sha3_256(hash_it.encode())
print(hashed.hexdigest())
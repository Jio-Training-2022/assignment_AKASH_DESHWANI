# Given a user_input as a string, calculate its md5 hash


# This hash function accepts sequence of bytes and returns 128 bit hash value,
# usually used to check data integrity but has security issues.

import hashlib
if __name__ == "__main__":
    user_ip = input("enter a string:")
    result = hashlib.md5(user_ip.encode())

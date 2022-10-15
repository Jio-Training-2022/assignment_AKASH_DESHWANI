# Encode a string by adding 10 to all the ascii characters of that string and decode it back 

def encode_string(string):
    encoded_string = ""
    for char in string:
        encoded_string += chr(ord(char) + 10)
    return encoded_string

def decode_string(string):
    decoded_string = ""
    for char in string:
        decoded_string += chr(ord(char) - 10)
    return decoded_string

if __name__ == "__main__":
    string = input("Enter a string: ")
    encoded_string = encode_string(string)
    print("Encoded string: ", encoded_string)
    decoded_string = decode_string(encoded_string)
    print("Decoded string: ", decoded_string)
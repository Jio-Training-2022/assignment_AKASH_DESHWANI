# Use a function from another file 


from HW_day13_q18 import encode_string, decode_string

if __name__ == "__main__":
    string = input("Enter a string: ")
    encoded_string = encode_string(string)
    print("Encoded string: ", encoded_string)
    decoded_string = decode_string(encoded_string)
    print("Decoded string: ", decoded_string)
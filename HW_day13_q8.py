# Take user input and write it to a file. 

if __name__ == "__main__":
    with open("user_input.txt", "w") as file:
        while True:
            user_input = input("Enter text: ")
            if user_input == "exit":
                break
            file.write(user_input + "")


# Calculate how many times a string occurs in a given file.


if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as file:
        data = file.read()
    occurrences = data.count("python")

    print('Number of occurrences of the word :', occurrences)
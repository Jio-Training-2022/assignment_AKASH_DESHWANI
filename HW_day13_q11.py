# Calculate the weight of the word banana.(weight = sum of ascii values of all characters )

if __name__ == "__main__":
    word = "banana"
    weight = 0
    for char in word:
        weight += ord(char)
    print(f"Weight of the word {word} is {weight}")

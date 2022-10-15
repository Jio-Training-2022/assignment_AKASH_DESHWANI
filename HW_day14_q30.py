# Given the name strings in a file, read all the names, convert them to corresponding ascii characters and calculate the sum

if __name__ == "__main__":
    with open('d:/Study/AI_DS/1_Term/05_Python/python_Statusneo/Code/scripts/names.txt') as f:
        names = f.read().splitlines()
        # convert the names to corresponding ascii characters
        names = [ord(name) for name in names]
        names = [sum(name) for name in names ]
        print(names)
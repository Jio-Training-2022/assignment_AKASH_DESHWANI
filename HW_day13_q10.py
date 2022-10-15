# Fetch the data from a url and calculate the number of strings in it. 
import requests as req
import pdb

if __name__ == "__main__":
    resp = req.get("https://medium.com/@akashdeshwani/python-tuples-and-lists-a-beginners-guide-7320b3f2128a")
    with open("text.txt", "w", encoding="utf-8") as file:
        file.write(resp.text)

    with open("text.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line)

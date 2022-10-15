# Marks of a student are given in a file, calculate the average marks.


if __name__ == "__main__":
    with open("D://Study//AI_DS//1_Term//05_Python//python_Statusneo//Code//scripts//marks.txt", "r") as marks:
        lines = marks.readlines()
        total = 0
        for line in lines:
            total += int(line)
        print("Average marks: ", total / len(lines))

# Given a file with numbers , calculate mean, median and mode.
import pdb 

if __name__ == "__main__":
    with open("D://Study//AI_DS//1_Term//05_Python//python_Statusneo//Code//scripts//marks.txt", "r") as marks:
        lines = marks.readlines()
        total = 0
        data = []
        for line in lines:
                data.append(int(line))
                total += int(line)
        print("Average marks: ", total / len(lines))
        mode = max(set(lines), key=lines.count)
        print("Mode: ", mode)
        # pdb.set_trace()
        data.sort()
        if len(data) % 2 == 0:
            median = (int(data[len(data) // 2]) + int(data[(len(data) // 2) - 1])) / 2
        else:
            median = int(data[len(data) // 2])
        print("Median: ", median)


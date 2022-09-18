# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.


# link -> https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# code 

if __name__ == '__main__':
    tstudents = int (input("Enter total no. of students : "))
    records = []
    for i in range(tstudents):
        name = input("Enter name of student: ")
        score = float(input("Enter grade of student:"))
        records.append([name,score])
    print (records)

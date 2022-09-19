# link -> https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
    [print(names) for names in sorted([name for name,
     tests in l if tests == 
     sorted(list(set([tests for name, tests in l])))[1]])]
# Build a simple school which allows for :: 
# 3.1 Adding a new student to a class with a Name & (unique) ID 
# 3.2 Showing total number of students in a class 
# 3.3 Removing the name of a student from a class 
# 3.4 Promoting a student to the next grade

def newstudent (dic,grade):
    stud_id = input ("Enter new student id :")
    if stud_id in dic.keys():
        print("Student already exits.")
        print("Student name and Student ID and student grade ", dic[stud_id], stud_id , grade[stud_id])
    else:
        stud_name = input ("Enter new student Name :")
        stud_grade = input ("Enter new student grade :")
        dic[stud_id] = stud_name
        dic[stud_id] = stud_grade
    print ("New Student ID and Student Name and grade : ", stud_id, stud_name, grade[stud_id])
    return(dic,grade)

def totalstud(dic):
    print("total no. of student :", len(dic))

def removestud(dic):
    stud_id = input ("Enter student id to remove student :")
    print("Name of Student who is removed ", dic.pop(stud_id))
    return(dic)

def promtstud(dic,grade):
    stud_id = input ("Enter student id to promot : ")
    print("Student name: ",dic[stud_id]," Current grade of the student :", grade[stud_id])
    grade[stud_id] = input ("Enter new grade: ")
    return (grade)


if __name__ == "__main__":
    exit_condition = False
    Stud_data = {}
    Stud_grade = {}
    while (exit_condition != True):
        val = val = int(input("\n Welcome to Py Bank: \n Select the options \n To add new student: Enter -> 1 \n To remove student: Enter -> 2 \n To promte student: Enter -> 3 \n To display total no. of students:  Enter -> 4 \n To EXIT: Enter -> 5 \n input:"))
        if (val == 1):
            Stud_data = newstudent(Stud_data,Stud_grade)
        elif (val == 2):
            Stud_data = removestud(Stud_data)
        elif (val == 3):
            Stud_grade = promtstud(Stud_data,Stud_grade)
        elif (val == 4):
            totalstud(Stud_data)
        else:
            exit_condition = True
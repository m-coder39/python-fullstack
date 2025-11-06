def AddStudent():
    f=open('students.txt','a')
    name=input("enter student name")
    marks=int(input("enter marks"))
    f.write(f"{name}:{marks}\n")
    print("student record added successfully")
    f.close()

def ViewAllStudents():
    f=open('students.txt','r')
    print("All students:\n"+f.read())
    f.close()

def SearchStudent():
    name=input("enter name of the student to be searched for:")
    f=open('students.txt','r')
    for line in f:
        if ':' in line:
            names, marks = line.split(':')
            if (name.lower() == names.lower()):
                print("found")
                break
    else:
        print("not found")



    f.close()

def AverageMarks():
    f = open('students.txt', 'r')
    sum=0
    for line in f:
        if ':' in line:
            names, marks = line.split(':')
            sum+=int(marks)
    avg=sum/len(marks)
    print("Average=",avg)





print("===== Student Marks Management System =====\n1. Add Student Record\n2. View All Students\n3. Search Student\n4. Calculate Average Marks\n5. Exit")
ch=int(input("enter your choice"))
if ch==1:
    AddStudent()
elif ch==2:
    ViewAllStudents()
elif ch==3:
    SearchStudent()
elif ch==4:
    AverageMarks()
elif ch==5:
    exit()

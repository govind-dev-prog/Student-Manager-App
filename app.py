student={}

while True:
    print("\n......Student Manager App.....")
    print("1.Add the student")
    print("2.View all student")
    print("3.Check Result")
    print("4.Exit")

    choice = input("enter your choice:")

    #Add student
    if choice=="1":
        name = input("enter student name:")
        marks = int(input("enter mark:"))
        student[name] = marks
        print(f"{name} Successfully Added!")

    #view student
    elif choice =="2":
        if not student:
            print("NO Student found!")
        else:
            for name ,marks in student.items():
                print(name, ":", marks)

    #check result
    elif choice =="3":
        name = input("enter student name:")
        if name in student:
            marks=student[name]
            if marks>=40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found")        

    #exit
    elif choice =="4":
        print("Exiting......")
        break
    else:
        print("In-valid input")


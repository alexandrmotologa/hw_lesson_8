# Students dict: names, speciality, grades

students = [
    {'name': 'Ion Drop', 'specs': 'IT', 'grades': 9.567},
    {'name': 'Tatiana Hush', 'specs': 'Filology', 'grades': 9.667},
    {'name': 'Maria Nush', 'specs': 'Filology', 'grades': 8.001},
    {'name': 'John Doe', 'specs': 'Management', 'grades': 9.099},
    {'name': 'Steven Banderas', 'specs': 'Law', 'grades': 9.121},
    {'name': 'Fred Oleson', 'specs': 'IT', 'grades': 9.101},
    {'name': 'Christina Martin', 'specs': 'IT', 'grades': 9.888},
    {'name': 'Joe Statham', 'specs': 'Education', 'grades': 9.111},
    {'name': 'Willie Zuckerberg', 'specs': 'Nothing', 'grades': 10.000},
]


# ERROR NOT FOUND

def not_found():
        print("##### ERROR ##### STUDENT NOT FOUND! ##### TRY AGAIN ##### ERROR #####")
        return False


# func print name, specs, grades

def display_st():
    for i in range(len(students)):
        print(f'='*150)
        print(f" >> {students[i]['name']:30s}  {students[i]['specs']:20s} {students[i]['grades']:4.2f}")
        print(f'='*150)


# 1. Show Students List

def read():
    for i in range(len(students)):
        print(f'='*150)
        print(f" > {students[i]['name']:30s}  {students[i]['specs']:20s}")
        # print(students[i].get('name') students[i].get('specs'))
        # alta varianta de a extrage i din dict
        print(f'='*150)


# 1.1. Show Students List Details

def read_details():
    display_st()


# 1.2. Show Students List with Details in Alphabetic Order

def read_alphabetic():
    for j in range(len(students)):
        for i in range(len(students) - 1):
            if students[i]['name'] > students[i + 1]['name']:
                temp = students[i]
                students[i] = students[i + 1]
                students[i + 1] = temp
    display_st()


# 1.3. Show Students List with Details in Grades Order

def bubble_sort_grades(order='1'):
    if order == '1':
        for j in range(len(students)):
            for i in range(len(students) - 1):
                if students[i]['grades'] < students[i + 1]['grades']:
                    temp = students[i]
                    students[i] = students[i + 1]
                    students[i + 1] = temp
    if order == '2':
        for j in range(len(students)):
            for i in range(len(students) - 1):
                if students[i]['grades'] > students[i + 1]['grades']:
                    temp = students[i]
                    students[i] = students[i + 1]
                    students[i + 1] = temp
    if len(order.strip()) == 0:
        pass
    else:
        pass
    display_st()


def sort_grades():
    print(f' #####'*15, '\n')
    print("If you want in ascending order type 1\n")
    print("If you want in descending order type 2\n")
    print("If you want in order of registration in the system, press ENTER\n")
    print(f'#####'*15)
    bubble_sort_grades(input(">>>"))


# 2. Show Student Details

def details():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students)):
        if students[i]['name'] == name:
            print("STUDENT FOUND!")
            print(f'='*150)
            print(f"{students[i]['name']:30s}   {students[i]['specs']:20s}  {students[i]['grades']:4.2f}")
            print(f'='*150)
            return True
    else:
        not_found()


# 3. Edit Student Details
# de optimizat codul

def edit():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students)):
        if students[i]['name'] == name:
            print("STUDENT FOUND!")

            new_name = input(" ENTER THE STUDENT'S NAME > ").lower().title()
            if len(new_name.strip()) == 0:
                new_name = students[i]['name']
            else:
                students[i]['name'] = new_name
                print("THE NAME HAS BEEN EDITED")

            new_spec = input(" ENTER THE STUDENT'S SPECIALITY > ").lower().title()
            if len(new_spec.strip()) == 0:
                new_spec = students[i]['specs']
            else:
                students[i]['specs'] = new_spec
                print("THE SPECIALITY HAS BEEN EDITED")

            try:
                new_grade = float(input(" ENTER THE STUDENT'S GRADE > "))
                if new_grade > 10 or new_grade < 0:
                    print("##### ERROR ##### The lowest grade in educational system is (1), the highest is (10) ##### ERROR #####")
                    break
                else:
                    students[i]['grades'] = new_grade
                    print("THE GRADE HAS BEEN EDITED")
            except ValueError:
                break
            return True
    else:
        not_found()


# 4. Delete Student

def delete():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students)):
        if students[i]['name'] == name:
            print("STUDENT DELETED!")
            del students[i]
            return True
    else:
        not_found()


# 5. ADD NEW Student

def new_student():
    try:
        new_name = input(" THE NAME AND SURNAME OF THE NEW STUDENT > ").lower().title()
        new_spec = input(" STUDENT SPECIALTY > ").lower().title()
        new_grade = float(input(" STUDENT GRADE > > "))
        if len(new_name.strip()) != 0 and len(new_spec.strip()) != 0 and new_grade <= 10 and new_grade > 0:
            students.append({
                'name': new_name,
                'specs': new_spec,
                'grades': new_grade,
                })
            print("STUDENT ADD!")
        else:
            print("PLEASE ENTER STUDENT GRADE")
            return False
    except:
        print('ERROR, THE DATA WAS ENTERED INCORRECTLY')


# MENU

def menu():
    option = - 1
    try:
        while option != 0:
            print("\n\n")
            print("########## MENU ##########")
            print("> 1. Show Students List")
            print(">>\t1.1. Show Students List with Details")
            print(">>\t1.2. Show Students List with Details in Alphabetic Order")
            print(">>\t1.3. Show Students List with Details in Grades Order")
            print("> 2. Show Student Details")
            print("> 3. Edit Student Details")
            print("> 4. Delete Student")
            print("> 5. ADD NEW Student")
            print("> 0. Exit")
            print("##########################")
            print("CHOOSE OPTION > ")

            option = float(input())

            if option == 1:
                read()
            if option == 1.1:
                read_details()
            if option == 1.2:
                read_alphabetic()
            if option == 1.3:
                sort_grades()
            if option == 2:
                details()
            if option == 3:
                edit()
            if option == 4:
                delete()
            if option == 5:
                new_student()
            if option > 5 or option <= -1:
                print("##### ERROR ##### TRY AGAIN ##### ERROR #####")
                menu()
            if option == 0:
                print("##### GOODBYE ##### EXIT ##### GOODBYE #####")
    except ValueError:
        menu()
menu()

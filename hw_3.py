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

ADMIN = "Sarah Connor"
PASSWORD = "dadada123"


def not_found():
        print("##### ERROR ##### STUDENT NOT FOUND! ##### TRY AGAIN ##### ERROR #####")
        return False


def read():
    for i in range(len(students)):
        print(f"{students[i]['name']:30s}  {students[i]['specs']:20s}") 


def details():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students)):
        if students[i]['name'] == name:
            print("STUDENT FOUND!")
            print(f"{students[i]['name']:30s}   {students[i]['specs']:20s}  {students[i]['grades']:10.2f}")            
            return True
    else:
        not_found()


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


# de incercat cu functia pop()

def delete():
    name = input(" Which student? > ").lower().title()
    for i in range(len(students)):
        if students[i]['name'] == name:
            print("STUDENT DELETED!")
            del students[i]
            return True
    else:
        not_found()


#de facut restrictii '' + ' ' 
    
def new_student():
        students.append({
            'name': input(" THE NAME AND SURNAME OF THE NEW STUDENT > ").lower().title(),
            'specs': input(" STUDENT SPECIALTY > ").lower().title(),
            'grades': float(input(" STUDENT GRADE > ")),
            })
        print("STUDENT ADD!")


def admin():
    admin_try = 0
    while admin_try < 3:
        admin = input("Your Acc:")
        if admin != ADMIN:
            admin_try += 1
        if admin == ADMIN:
            password = input("Your pass:")
            if password == PASSWORD:
                print(f"##### WELCOME {ADMIN} #####")
                menu()
        if password != PASSWORD:
            admin_try += 1
    else:
        print("WRONG LOGIN/PASSWORD")


def menu():
    option = - 1
    try:
        while option != 0:
            print("\n\n")
            print("########## MENU ##########")
            print("1. Show Students List")
            print("2. Show Student Details")
            print("3. Edit Student Details")
            print("4. Delete Student")
            print("5. ADD NEW Student")
            print("0. Exit")
            print("##########################")
            print("CHOOSE OPTION > ")

            option = int(input())

            if option == 1:
                read()
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
                print("##### EXIT #####")
    except ValueError:
        menu()

admin()

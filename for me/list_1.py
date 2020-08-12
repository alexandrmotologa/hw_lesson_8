

# Student lists: names, speciality, grades

student_names = ["Ion Drop", "Tatiana Hush", "Maria Nush", "John Doe", "Steven Banderas", "Fred Oleson", "Christina Martin", "Joe Statham", "Willie Zuckerberg"]
student_specs = ["IT", "Filology", "Filology", "Management", "Law", "IT", "IT", "Education", "Nothing"]
student_grades = [9.567, 9.667, 8.001, 9.099, 9.121, 9.101, 9.888, 9.111, 10.000]


# ERROR NOT FOUND

def not_found():
        print("##### ERROR ##### STUDENT NOT FOUND! ##### TRY AGAIN ##### ERROR #####")
        return False


#1. Show Students List

def read():
    for i in range(len(student_names)):
        print(f'-'*150)
        print(f" >> {student_names[i]:30s}")
        print(f'-'*150)


#1.1. Show Students List Details

def read_details():
    for i in range(len(student_names)):
        print(f'-'*150)
        print(f" >> {student_names[i]:30s} ( {student_specs[i]:10s} ) {student_grades[i]:4.1f}")
        print(f'-'*150)


#2. Show Student Details

def details():
    name = input(" Which student? > ").lower().title()
    for i in range(len(student_names)):
        if student_names[i] == name:
            print("STUDENT FOUND!")
            print(f'-'*150)
            print(f" >>> {student_names[i]:30s} ( {student_specs[i]:2s} ) {student_grades[i]:4.1f}")
            print(f'-'*150)
            return True
    else:
        not_found()


#3. Edit Student Details
# de optimizat codul

def edit():
    name = input(" Which student? > ").lower().title()
    for i in range(len(student_names)):
        if student_names[i] == name:
            print(f"STUDENT FOUND! {student_names[i].upper()}")

            new_name = input(" ENTER THE STUDENT'S NAME > ").lower().title()
            if len(new_name.strip()) == 0:
                new_name = student_names[i]
            else:
                student_names[i] = new_name
                print("THE NAME HAS BEEN EDITED")

            new_spec = input(" ENTER THE STUDENT'S SPECIALITY > ").lower().title()
            if len(new_spec.strip()) == 0:
                new_spec = student_specs[i]
            else:
                student_specs[i] = new_spec
                print("THE SPECIALITY HAS BEEN EDITED")

            try:
                new_grade = float(input(" ENTER THE STUDENT'S GRADE > "))
                if new_grade > 10 or new_grade < 0:
                    print("##### ERROR ##### The lowest grade in educational system is (1), the highest is (10) ##### ERROR #####")
                    break
                else:
                    student_grades[i] = new_grade
                    print("THE GRADE HAS BEEN EDITED")
            except ValueError:
                break
            return True
    else:
        not_found()


#4. Delete Student

def delete():
    name = input(" Which student? > ").lower().title()
    for i in range(len(student_names)):
        if student_names[i] == name:
            print(f"{student_names[i].upper()}\t--->\tSTUDENT DELETED!")
            student_names.pop(i)
            student_specs.pop(i)
            student_grades.pop(i)
            return True
    else:
        not_found()


#5. ADD NEW Student

def new_student():
    try:
        name = input(" THE NAME AND SURNAME OF THE NEW STUDENT > ").lower().title()
        spec = input(" STUDENT SPECIALTY > ").lower().title()
        grade = float(input(" STUDENT GRADE > "))
        if len(name.strip()) == 0 and len(spec.strip()) == 0:
            print("ERROR, THE DATA WAS ENTERED INCORRECTLY")
        if len(name.strip()) == 0:
            print("PLEASE ENTER THE NAME AND SURNAME OF THE NEW STUDENT")
            return False
        if len(spec.strip()) == 0:
            print("PLEASE ENTER STUDENT SPECIALTY")
            return False
        elif grade <= 10 and grade > 0:
            student_names.append(name)
            student_specs.append(spec)
            student_grades.append(grade)
            print("STUDENT ADD!")
            return True
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
            print("1. Show Students List")
            print(">> 1.1. Show Students List with Details")
            print("2. Show Student Details")
            print("3. Edit Student Details")
            print("4. Delete Student")
            print("5. ADD NEW Student")
            print("0. Exit")
            print("##########################")
            print("CHOOSE OPTION > ")
            
            option = float(input())
            
            if option == 1:
                read()
            if option == 1.1:
                read_details()
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
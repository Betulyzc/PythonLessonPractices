# Grade Application

# 1- Menu
#    1- Enter Grade
#    2- Show Grades
#    3- Save Grades
#    4- Exit

# Grading Scale:
#    90-100 -> AA
#    80-89  -> BA
#    75-79  -> BB
#    70-74  -> CB
#    65-69  -> CC
#    60-64  -> DC
#    50-59  -> DD
#    40-49  -> FD
#    0 -39  -> FF

def Menu():
    while True:
        print("\nMenu")
        print("   1- Enter Grade\n   2- Show Grades\n   3- Save Grades\n   4- Exit")

        try:
            selection = int(input("Please enter a value: "))
            if selection == 1:
                enterGrade()
                 
            elif selection == 2:
                showGrades()
                 
            elif selection == 3:
                saveGrades()
                
            elif selection == 4:
                print("Exiting...")
                break
            else:
                print("Invalid value. Please select a value between 1 and 4.")
        except ValueError:
            print("You entered an invalid character.")
                

def enterGrade():
    name = input("Student's name: ")
    surname = input("Student's surname: ")
    
    try:
        grade1 = int(input("Grade 1: "))
        grade2 = int(input("Grade 2: "))
        grade3 = int(input("Grade 3: "))
    except ValueError:
        print("Invalid grade input. Please enter numeric values.")
        return
    
    with open(r"C:\Users\LENOVO\OneDrive\Masaüstü\PythonLessonPractice\PythonProgramlamaDiliSadikTuran\StudentTracker\Exam_Grades.txt", "a", encoding="utf-8") as file:
        file.write(name + ' ' + surname + ':' + str(grade1) + ',' + str(grade2) + ',' + str(grade3) + '\n')
    print("Grade saved successfully!")


def calculateGrade(line):
    line = line.strip()
    if not line:
        return ""
    
    data = line.split(":")
    student_name = data[0]
    grades = list(map(int, data[1].split(",")))
    average = sum(grades) / len(grades)
    
    if 90 <= average <= 100:
        letter = "AA"
    elif 80 <= average < 90:
        letter = "BA"
    elif 75 <= average < 80:
        letter = "BB"
    elif 70 <= average < 75:
        letter = "CB"
    elif 65 <= average < 70:
        letter = "CC"
    elif 60 <= average < 65:
        letter = "DC"
    elif 50 <= average < 60:
        letter = "DD"
    elif 40 <= average < 50:
        letter = "FD"
    else:
        letter = "FF"
    
    return f"{student_name} : {letter} - ({average:.2f})\n"


def showGrades():
    try:
        with open(r"C:\Users\LENOVO\OneDrive\Masaüstü\PythonLessonPractice\PythonProgramlamaDiliSadikTuran\StudentTracker\Exam_Grades.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No grades recorded yet.")
                return
            for line in lines:
                print(calculateGrade(line), end="")
    except FileNotFoundError:
        print("No records found. Please enter grades first.")


def saveGrades():
    try:

        with open(r"C:\Users\LENOVO\OneDrive\Masaüstü\PythonLessonPractice\PythonProgramlamaDiliSadikTuran\StudentTracker\Exam_Grades.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("No grades to save.")
                return
        
        with open(r"C:\Users\LENOVO\OneDrive\Masaüstü\PythonLessonPractice\PythonProgramlamaDiliSadikTuran\StudentTracker\Final_Grades.txt", "w", encoding="utf-8") as output_file:
            for line in lines:
                output_file.write(calculateGrade(line))
        
        print("Grades have been saved successfully to Final_Grades.txt.")
    except FileNotFoundError:
        print("No records found to save. Please enter grades first.")


Menu()
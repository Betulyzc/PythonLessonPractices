# 1- Girilen 2 sayıdan hangisi büyüktür?
firstNumberInput=int(input("Please enter first number: "))
secondNumberInput=int(input("Please enter second number: "))

result=(firstNumberInput>secondNumberInput)
print(f"{firstNumberInput} greater than {secondNumberInput}: {result}"),

# 2- Girilen bir sayının tek çift kontrolünü yapınız.
number=int(input("Enter a number: "))
result= (number % 2 == 0)
print(f"{number} is a even: {result}")

# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı.
student={
    "name":"Betül",
    "surname":"Yazıcı",
    "grades":(int(input("not 1: ")),int(input("not 2: ")),int(input("not 3: ")))
}
average_grade=round((sum(student["grades"])/ len(student["grades"])) , 3)
print(f"{student['name']} {student['surname']} is a successful student in lesson: {average_grade >= 50}, (Average Grade: {average_grade})")

#    Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
#    ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
#    ** öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.

numberOfStudent=int(input("Please enter the number of students: "))
students=[]

index=0

while(index < numberOfStudent):
    studentNumber=int(input("Student Number: "))
    studentName=input("Name: ")
    studentSurname=input("Surname: ")

    students.append({
        "StudentNumber":studentNumber,
        "StudentName":studentName,
        "StudentSurname":studentSurname
    })  
    index+=1
    

for student in students:
    print(student) 


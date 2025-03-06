from datetime import datetime

# Aşağıdaki öğrenci bilgilerini dictionary listesinde saklayınız.
    # 101 Yiğit Bilgi 2010 (40,80,90)
    # 102 Ada Bilgi   2012 (80,80,80)
    # 103 Çınar Turan 2017 (70,70,70)

students={
    101:{
        "name":"Yiğit",
        "surname":"Bilgi",
        "birthyear":2010,
        "grades":(40,80,90)
     },
     102:{
         "name":"Ada",
         "surname":"Bilgi",
         "birthyear":2012,
         "grades":(80,80,80)
     },
     103:{
         "name":"Çınar",
         "surname":"Turan",
         "birthyear":2017,
         "grades":(70,70,70)
     }
}

# Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız.
    # 101 numaralı Yiğit Bilgi ismindeki öğrencinin yaşı 14 ve not ortalaması 70.

inputStudentNumber=int(input("Please enter a student number: "))
student=students[inputStudentNumber]
#averageGrade=round((student["grades"][0]+ student["grades"][1] + student["grades"][2]) /3 ,2)
averageGrade=round((sum(student["grades"])/ len(student["grades"])), 2)
age=datetime.now().year-student["birthyear"]

print(f"{inputStudentNumber} numaralı {student['name']} {student['surname']} ismindeki öğrencinin yaşı {age} ve not ortalaması {averageGrade} ")

from datetime import datetime

# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
cars=["Toyota","Bmw","Renault", "Mercedes"]

# 2- Liste kaç elemanlıdır?
print(f"Number of List Elements: {(len(cars))}")

# 3- Listenin ilk ve son elemanı nedir?
firstElement=cars[0]
lastElement=cars[-1]
print(f"First elements is {firstElement} and last elements is {lastElement} in list.")

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
#cars[2]="Togg"
cars[cars.index("Renault")]="Togg"
print(cars)

# 5- "Togg" listenin bir elemanı mıdır?
queryResult= "Togg" in cars
print("Togg is in cars: "+ str(queryResult))

# 6- Listenin ilk 2 elemanını alınız.
print(cars[:2])

# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
#cars=cars+["Ford","Citroen"]  
cars.extend(["Ford","Citroen"]) 
print(cars)

# 8- Listenin son elemanını siliniz.
#del cars[-1]
cars.pop() 
print(cars)

#9- Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

students=[["Yigit","Bilgi",2010,[70,80,90]], ["Ada","Bilgi",2011,[70,70,80]] ,["Çınar","Turan",2017,[60,60,90]]]
currentYear=datetime.now().year
for student in students:    
    print(student)

# 10- Öğrencilerin yaşlarını hesaplayınız.
Yigit_sAge = currentYear - students[0][2]
Ada_sAge = currentYear - students[1][2] 
Cinar_sAge = currentYear-students[2][2]

print(f"Yiğit is {Yigit_sAge} years old. \nAda is {Ada_sAge} years old. \nÇınar is {Cinar_sAge} years old.")


#9. ve 10. soruların daha iyi alternatif yöntemi.
for student in students:
    name, surname,birthyear,grades=student
    age=currentYear-birthyear
    average_grade=round(sum(grades) / len(grades),2)
    print(f"{name} {surname} is {age} years old. Average Grade is {average_grade}.")
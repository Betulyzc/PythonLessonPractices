title = "Python ile Programlama Dersleri"

# 1- 'title' değişkeni içerisindeki karakter sayısı nedir?
title_length = len(title)
print("title değişkeni karakter sayısı: " + str(title_length))

# 2- 'title' içerisindeki 'Python' kelimesini alın.
print(title[:6])  # ya da  print(title[0:6])

# 3- 'title' değişkeninin ilk 5 ve son 5 karakterini alın.
first_five_chars = title[:5]
last_five_chars = title[-5:]
print(f"First Five Characters: {first_five_chars}\nLast Five Characters: {last_five_chars}")

# 4- 'title' değişkenini tersten yazdırınız.
print(title[::-1])

# 5- Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.
#    Örnek: Çınar Turan isimli öğrencinin 1.notu 60, 2.notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

first_name = input("First Name: ")
last_name = input("Last Name: ")
grade_1 = int(input("Grade 1: "))
grade_2 = int(input("Grade 2: "))
average_grade = (grade_1 + grade_2) / 2

print(f"{first_name} {last_name} isimli öğrencinin 1. notu {grade_1}, 2. notu {grade_2} ve not ortalaması {average_grade:.2f} olarak hesaplanmıştır.")

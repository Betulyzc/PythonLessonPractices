# 1- Yaşı 18' den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

parent_permission = False
age = 18
result = (parent_permission) or (age >= 18)

# 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.
grade = 55
result = (50 <= grade <= 100)
print(f"Passing status: {result}")

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.
average = 75
weak_subject_count = 0
result = (average >= 70) and (weak_subject_count == 0)

# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.
education = "associate degree"
smoking = False

result = (education == "associate degree" or education == "bachelor's degree") and (not smoking)

# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.

email = "info@sadikturan.com"
username = "sadikturan"
password = "12345"

entered_info = input("Email or username: ")
entered_password = input("Password: ")

result = (email == entered_info or username == entered_info) and (password == entered_password)

print(result)
# 1- Faktöriyel fonksiyonu oluşturunuz ve fonksiyona gelen değer için hata mesajları verin.

def Factorial(number):
    try:
        if type(number) is not int:
            raise TypeError("TyperError:You did not enter an integer.")

        if(number<0):
            raise ValueError("ValueError: You entered a negative value.")
        result=1
        
        for index in range(1, number +1):
            result*=index
        
        return result

    except ValueError as error:
       return str(error)
    except TypeError as error2:
        return str(error2)

try:
    print(Factorial(2))
except NameError:
    print("NameError: You tried to access a variable that does not exist.")



#2- Girilen parola içinde türkçe karakter hatası veriniz.

def passwordCheck(password):
    turkish_characters = "şçğüöıİ"
    for char in password:
        if char not in turkish_characters:
            raise TypeError("Password cannot contain Turkish characters.")
        
    print("Valid password.")

password = input("Enter password: ")

try:
    passwordCheck(password)
except TypeError as e:
    print(e)
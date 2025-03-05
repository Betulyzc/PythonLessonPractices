"""
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    Alan: πr²
    Çevre: 2πr

    Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km / 1.609344
"""

# Uygulama 1
radius = float(input("Enter the radius: "))  
pi=3.14
area_result = pi * (radius ** 2)  
circumference_result = 2 * pi * radius  

print(f"Application 1 Output => Area: {area_result}, Circumference: {circumference_result}")

# Uygulama 2 
kilometer = float(input("Enter the distance in kilometers: "))  
mile = kilometer / 1.609344
mile = round(mile, 2)  # Virgülden sonrasını yuvarlama işlemi yapar.

print(f"Application 2 Output => Mile: {mile}")

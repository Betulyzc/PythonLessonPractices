import random


# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def printWord(word,repeat):
    return word*repeat

print(printWord("Hello",3))

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def calculateRectangleAreaAndPerimeter(width,height):
    rectangelArea=width*height
    rectangelPerimeter=2*(width+height)
    return f"Area: {rectangelArea}, Perimeter: {rectangelPerimeter}"

print(calculateRectangleAreaAndPerimeter(3,4))


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. 
def coinToss():
    result = random.choice(['Yazı', 'Tura'])
    return result

print(coinToss())

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def findPrimeNumber(number1, number2):
    for num in range(number1, number2 + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)

findPrimeNumber(10, 50)

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def findDivisors(number):
    divisors=[]
    for i in range(2,number+1):
        if(number % i==0):
            divisors.append(i)

    return divisors

print(findDivisors(15))


 



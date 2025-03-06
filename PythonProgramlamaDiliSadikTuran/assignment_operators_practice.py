a, b, c = 4, 8, (12, 2)

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?
firstNumberInput=int(input("Please enter first number: "))
secondNumberInput=int(input("Please enter second number: "))

sum_abc=a + b + (c[0] + c[1])
ınputsMultiply=firstNumberInput * secondNumberInput
result=ınputsMultiply - sum_abc


#2- c' nin b' ye kalansız bölümünü hesaplayınız.
result=sum(c)/b

# 3- (a,b,c) toplamının mod 7' si nedir?
result=(sum(c)+a+b) & 7

# 4- b' nin a. kuvvetini hesaplayınız.
result=b**a

#5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?
a, *b, c = (2,4,6,8,13) # c equals 13 
result=c**3 

# 6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?
a, b, *c = (2,4,6,8,13) # a=2  b=4  c=(6,8,13)
result=sum(c)

print(result)
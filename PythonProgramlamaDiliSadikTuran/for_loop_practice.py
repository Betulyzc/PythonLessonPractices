#Uygulama1
numbers = [3,5,7,2,12,32,45]


# 1- "numbers" listesindeki her bir elemanı yazdırınız.

"""
for number in numbers:
    print(number)
"""

# 2- "numbers" listesinde hangi sayılar 3' ün katıdır?

"""
for number in numbers:
    if(number % 3 == 0):
        print(number)
"""

# 3- "numbers" listesinde tüm sayıların toplamı nedir?
'''
sum=0
for number in numbers:
    sum+=number

print("Sum of numbers: "+ str(sum))
'''

#Uygulama 2

products = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "products" listesindeki tüm iphone marka ürünleri listeleyiniz. (find, index)
'''Way 1
for index in range(len(products)):
    productSplit=products[index].split(" ")
    if (productSplit[0] == "iphone"):
        print(products[index])

'''

'''Way 2 (Best Way)
for product in products:
    if (product.startswith("iphone")):
        print(product)

'''

'''Way 3
for product in products:
    index=product.find("iphone")
    if(index !=-1):
        print(product)

'''


     
# 5- "products" listesinde kaç adet samsung ürünü vardır?
count=0
for product in products:  
    if(product.startswith("samsung")):
        count+=1

print("Total Samsung Product Count: " + str (count))
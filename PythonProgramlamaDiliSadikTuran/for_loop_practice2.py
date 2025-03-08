products = [
    {"productName":"Hp Victus 1", "price": 32999},
    {"productName":"Lenovo ThinkPad", "price": 25499},
    {"productName":"Apple Macbook", "price": 49999},
    {"productName":"Huawei Matebook", "price": 26999},
    {"productName":"Casper Nirvana", "price": 20000},
    {"productName":"Hp Victus 2", "price": 30000},
]


# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#    "The price of the Hp Victus brand product is 32999 Turkish Liras."
for product in products:
    print(f"The price of the {product["productName"]} brand product is {product["price"]} Turkish Liras")


# 2- Ürünlerin fiyatları toplamı nedir?
totalCost=0
for product in products:
    totalCost+=product["price"]
print("Product total: "+str(totalCost))


# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.
print("Products  between 25000 and 40000: ")
for product in products:
    if (product["price"]>=25000 and product["price"]<=40000):
        print(f"{product['productName']} : {product['price']}")


# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.

wordInput=input("Please enter the products you are looking for: ").lower()
for product in products:
    if wordInput in product["productName"].lower():
        print(product)


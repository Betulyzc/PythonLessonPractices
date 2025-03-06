customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]

# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
customers.append("sadikturan")
order_totals.append(5000)

# 2- Son eklenen siparişi siliniz.
customers.pop()
order_totals.pop()

# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
    # '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır. (döngüler)

#print(f"Order total of customer named {customers[0]} is {order_totals[0]}.")
#print(f"Order total of customer named {customers[1]} is {order_totals[1]}.") # bunun gibi uzunca yazılabilir ama uzun.
 
#Kısa Yolu
for customer, order in zip(customers, order_totals):
    print(f"Order total of customer named {customer} is {order}")

# 4- Müşterileri alfabetik olarak sıralayınız.
customers.sort()

# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()
order_totals.reverse()

# 6- En düşük ve en yüksek sipariş hangisidir?
print(f"lowest order: {min(order_totals)}")
print(f"highest order: {max(order_totals)}")

# 7- 'sadikturan' isimli kullanıcının kaç tane siparişi vardır?
print(f"sadikturan order count: {customers.count("sadikturan")}")

# 8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.
customers.remove("ahmetyilmaz")

# 9- Listelerdeki tüm içerikleri siliniz.
#customers.clear()
#order_totals.clear()

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.
nameInput=input("Name: ")
customerOrderTotalInput=int(input("total order:"))
customers.append(nameInput)
order_totals.append(customerOrderTotalInput)

print(customers)
print(order_totals)
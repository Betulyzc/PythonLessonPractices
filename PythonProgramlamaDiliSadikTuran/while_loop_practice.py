# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.
'''
starting_value_input=int(input("Please enter the starting value: "))
ending_value_input=int(input("Please enter the ending value: "))


index=starting_value_input
while(index< ending_value_input):
    if(index % 2 == 0):
        print(index)
    index+=1
'''

# 2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.
index=100
while(index>0):
    print(index)
    index-=1

# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
index=0
userGivenInputs=[]
while(index<5):
    number=int(input("Please enter number:"))
    userGivenInputs.append(number)
    index+=1
userGivenInputs.sort()
print(userGivenInputs)

# 4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.
username=""
while not username: #username boşsa döndü devam eder
    username=input("username: ")
print("girilen username: "+username)

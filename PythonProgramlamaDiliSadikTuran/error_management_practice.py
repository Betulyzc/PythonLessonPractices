list = ["1","3","5","20b","abc","10a","60"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

for x in list:
    try:
        result=int(x)
        print(result)
    except ValueError:
        continue

# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.

while True:
    
    valueInput=input("Please enter a integer or float value.( For exitting press 'q'): ")     
    if (valueInput =='q'):
        break
    try:    
        sonuc=float(valueInput)
        print(f"Input Value: {valueInput}")
        break

    except ValueError:
        print("Invalid value!")
        continue

# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonu hazırlayınız.
product = {"productName":"samsung s20","cost":10000}
def get(list,key):
    try:
        return list[key]
    except KeyError:
        return None

result=get(product, "cost")
result=get(product,"productName")
print(result)




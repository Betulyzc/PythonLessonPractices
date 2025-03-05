# User Information
first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email: ")
city = input("City: ")
vat_rate = 0.18

product_name1 = "Wireless Mouse"
product_price1 = 550

product_name2 = "Wireless Keyboard"
product_price2 = 650

product_name3 = "Laptop"
product_price3 = 55000

total_price = product_price1 + product_price2 + product_price3
total_price_with_vat = total_price * vat_rate

print(f"Total Price (including VAT): {total_price + total_price_with_vat:.2f}")

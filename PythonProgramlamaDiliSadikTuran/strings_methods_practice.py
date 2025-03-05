course_name = "Btk Akademi Python ile Programlama Dersleri çalışmaları"
website_url = "https://www.btkakademi.gov.tr/"

# 1- ' Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.
original_text = " Btk Akademi "
trimmed_text = original_text.strip()
print(original_text)
print(trimmed_text)

# 2- course_name değişkenindeki tüm karakterleri küçük harfe çeviriniz.
lower_text = course_name.lower()
print(lower_text)

# 3- website_url değişkeninde kaç tane '.' karakteri vardır?
dot_count = website_url.count('.')
print(dot_count)

# 4- website_url değişkeni 'https' ile mi başlıyor?
is_https = website_url.startswith('https')
print(is_https)

# 5- website_url 'tr' ile mi bitiyor?
is_tr = website_url.endswith('tr')
print(is_tr)

# 6- course_name içerisindeki tüm karakterler harflerden mi oluşuyor?
is_alpha = course_name.isalpha()  # Boşluk karakteri false yapar.
print(is_alpha)

# 7- course_name değişkenindeki tüm boşlukları '-' ile değiştiriniz.
replaced_spaces = course_name.replace(" ", "-")
print(replaced_spaces)

# 8- course_name değişkenindeki Python kelimesini ReactJs ile değiştiriniz.
replaced_python = course_name.replace("Python", "ReactJs")
print(replaced_python)

# 9- website_url değişkeni 'www' içeriyor mu?
found_www = website_url.find('www')
print(found_www)

# İkisi de aranan kelime varsa ilk geçtiği indeksi döndürür.
# find bulamazsa -1 döndürür hata vermez, index ValueError verir.
found_index = website_url.index('www')
print(found_index)

# course_name değişkenini listeye çevirir.
split_text = course_name.split()
print(split_text)
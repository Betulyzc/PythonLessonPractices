# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

exam1 = float(input("Exam 1: "))
exam2 = float(input("Exam 2: "))
project = float(input("Project: "))

average = (exam1 + exam2 + project) / 3

if (0 <= average < 25):
    print(f"Your average: {average} and your grade: 0")
elif (25 <= average < 45):
    print(f"Your average: {average} and your grade: 1")
elif (45 <= average < 55):
    print(f"Your average: {average} and your grade: 2")
elif (55 <= average < 70):
    print(f"Your average: {average} and your grade: 3")
elif (70 <= average < 85):
    print(f"Your average: {average} and your grade: 4")
elif (85 <= average <= 100):
    print(f"Your average: {average} and your grade: 5")
else:
    print("Invalid grade input")
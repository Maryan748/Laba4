import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

a = float(input("Введіть довжину сторони a: "))
b = float(input("Введіть довжину сторони b: "))
c = float(input("Введіть довжину сторони c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Рівносторонній трикутник")
    elif a == b or b == c or a == c:
        print("Рівнобедрений трикутник")
    else:
        print("Різносторонній трикутник")
else:
    print("Трикутник не існує")

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

age = int(input("Введіть кількість прожитих років: "))

if age < 6:
    print("Ще не школяр")
elif 6 <= age <= 9:
    print("Початкова школа")
elif 10 <= age <= 15:
    print("Середня школа")
elif 16 <= age <= 17:
    print("Старша школа")
else:
    print("Вже не школяр")

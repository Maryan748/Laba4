import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє числоgh: "))

unique_numbers = len(set([a, b, c]))

if unique_numbers == 1:
    print(3)
elif unique_numbers == 2:
    print(2)
else:
    print(0)

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))

are_odd = (A % 2 != 0) and (B % 2 != 0)
is_negative_difference = (A - B) < 0

if are_odd and is_negative_difference:
    print("Висловлювання істинне: Кожне з чисел A і B непарне, їх різниця — від'ємне число.")
else:
    print("Висловлювання хибне.")

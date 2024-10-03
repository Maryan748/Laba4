import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

bracket = input("Введіть символ дужки: ")

if bracket == '(' or bracket == ')':
    print("Кругла дужка")
elif bracket == '{' or bracket == '}':
    print("Фігурна дужка")
elif bracket == '[' or bracket == ']':
    print("Квадратна дужка")
else:
    print("Це не дужка")

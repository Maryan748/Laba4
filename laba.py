import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

week_number = int(input("Введіть номер тижня (1-2): "))
day_number = int(input("Введіть день тижня (1-7): "))

if week_number == 1:
    if day_number == 1:
        print("Понеділок: Математика")
    elif day_number == 2:
        print("Вівторок: Фізика")
    elif day_number == 3:
        print("Середа: Хімія")
    elif day_number == 4:
        print("Четвер: Біологія")
    elif day_number == 5:
        print("П’ятниця: Інформатика")
    elif day_number == 6:
        print("Субота: Англійська")
    else:
        print("Неділя: Вихідний")
elif week_number == 2:
    if day_number == 1:
        print("Понеділок: Географія")
    elif day_number == 2:
        print("Вівторок: Історія")
    elif day_number == 3:
        print("Середа: Математика")
    elif day_number == 4:
        print("Четвер: Фізика")
    elif day_number == 5:
        print("П’ятниця: Хімія")
    elif day_number == 6:
        print("Субота: Біологія")
    else:
        print("Неділя: Вихідний")

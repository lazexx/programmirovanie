a = int(input())
if a % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
if a > 0:
    print("Положительное")
elif a < 0:
    print("Отрицательное")
else:
    print("Ноль")
if 10 <= a <= 50:
    print("Принадлежит диапазону от 10 до 50")
else:
    print("Не принадлежит диапазону от 10 до 50")
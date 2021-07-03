import random

number = random.randint(0, 101)

while True:
    x = input("Введите число: ")
    if x == "" or x == "exit":
        break

    if not x.isdigit():
        print("Введите правильно число")
        continue

    user_answer = int(x)

    if user_answer > number:
        print("Загаданное число меньшеs")
    elif user_answer < number:
        print("Загаданное число больше")
    else:
        print("Совершенно верно!")
        break
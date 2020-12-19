import random


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


NUM = "number"
k = "0"
spisok = []
while not isint(NUM):
    NUM = input("Введите количество бочонков: ")

N = int(NUM)

for i in range(1, N + 1):
    spisok.append(i)

random.shuffle(spisok)

for i in range(N):
    k = input("Нажмите Enter для того, чтобы вытащить бочонок ")
    if k == "":
        print(spisok[i])
    else:
        while k != "":
            k = input("Нажмите Enter для того, чтобы вытащить бочонок ")
        print(spisok[i])

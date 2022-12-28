import random


def create_equation():
    degree = int(input('Введите максимальную степень: '))
    equation = {} # пустой словарь
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-1, 1)
    return equation
import random

# Генерируем словарь из степени и коэфицентов и записываем результат в словарь
def create_equation():
    degree = int(input('Введите максимальную степень: '))
    equation = {} # пустой словарь
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-100, 100)
    return equation


# Переводим словарь в строку, где ключи - степень, а значение - число 
def decode(equation: dict) -> str:
    new_equation = []
    for key, value in equation.items():# .valuse - по значениям, items - и ключи, и значения 
        if value != 0: 
         new_equation.append(f'{value}*x^{key}') # строчку возвращаем в список
    new_equation =' ' + ' + '.join(new_equation) + ' = 0'                 # убираем все не нужные символы
    new_equation = new_equation.replace('+ -', '- ') \
        .replace('*x^0', '').replace(' 1*x', ' x').replace('-1*x', '-x').replace('x^1', 'x')
    return new_equation[1:]


# переводим строку опять в словарь, где возвращаем значение 1, для сложения в дальнейшем
def encode(equation: str) -> dict:
    equation = (' ' + equation).replace(' + ', ' ').replace(' - ', ' -').replace('-x',' -1*x').replace(' x', ' 1*x')\
        .replace('*x ', '*x^1 ').split()[:-2]
    dict_equation = {}
    for item in equation[1:]:
        i = item.split('*x^')
        if len(i) > 1:
            dict_equation[int(i[1])] = int(i[0])
        elif len(i) == 1 and i[0] != '':
            dict_equation[0] = int(i[0])
    return dict_equation




# Складываем два словоря
def addition (first_eq: dict, second_eq: dict):
    final_eq = {}
    final_eq.update(first_eq) # обновляет словарь элементами из другого объекта словаря или из итерируемых пар ключ-значение
    final_eq.update(second_eq)


    for key in final_eq:
        final_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0) # складываем ключи
    return final_eq


# создаем 2 файла, куда помещаем 2 уравнения, в 3 файл - записываем результат сложения
def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


equation1 = create_equation()
equation2 = create_equation()
str_eq1 = decode(equation1)
str_eq2 = decode(equation2)
print(str_eq1)
print(str_eq2)
dict_eq1 = encode(str_eq1)
dict_eq2 = encode(str_eq2)
dict_final = addition(dict_eq1, dict_eq2)
str_final = decode(dict_final)
print(str_final)

write_file('first_file.txt', str_eq1)
write_file('second_file.txt', str_eq2)
write_file('addition_file..txt', str_final)
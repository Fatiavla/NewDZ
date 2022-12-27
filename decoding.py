

def decode(equation: dict) -> str:
    new_equation = []
    for key, value in equation.items():# .valuse - по значениям, items - и ключи, и значения 
        if value != 0: 
         new_equation.append(f'{value}*x^{key}') # строчку возвращаем в список
    new_equation =' ' + ' + '.join(new_equation) + ' = 0'                 # убираем все не нужные символы
    new_equation = new_equation.replace('+ -', '- ') \
        .replace('*x^0', '').replace(' 1*x', ' x').replace('-1*x', '-x').replace('x^1', 'x')
    # if new_equation.startswith('1*x'):
    #     return new_equation[2:]
    # elif new_equation.startswith('-1*x'):
    #     return new_equation.replace('-1*', '-')
    # else:
    return new_equation[1:]


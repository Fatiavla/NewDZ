

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
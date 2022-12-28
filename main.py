from create import create_equation
from decoding import decode
from encoding import encode
from addition import addition



def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)
  


if __name__ == '__main__':
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
    # print(equation) 
    # str_equation = decode(equation) # Словарь передаем в декод ( в строку)
    # print(str_equation)
    # dict_equation = encode(str_equation) # Строку в символы
    # print(dict_equation)  

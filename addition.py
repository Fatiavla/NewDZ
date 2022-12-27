


def addition (first_eq: dict, second_eq: dict):
    final_eq = {}
    final_eq.update(first_eq)
    final_eq.update(second_eq)


    for key in final_eq:
        final_eq[key] = first_eq.get(key, 0) + second_eq.get(key, 0) # складываем ключи
    return final_eq
        
        
        
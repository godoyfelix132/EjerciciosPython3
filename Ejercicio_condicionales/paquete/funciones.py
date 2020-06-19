def type_num(n):
    if n:
        if n > 0:
            return "positivo"
        else:
            return "negativo"
    else:
        return "cero"


def even_odd(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"


def prime(n):
    if n < 1:
        return "no es primo"
    elif n == 2:
        return "es primo"
    else:
        for i in range(2, n):
            if n % i == 0:
                return "no es primo"
        return "es primo"


def leap_year(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return 'es bisiesto'
            else:
                return 'no es bisiesto'
        else:
            return 'es bisiesto.'
    else:
        return 'no es bisiesto.'


def sort_list(list_sort):
    for j in range(len(list_sort)-1,0,-1):
        for i in range(j):
            if list_sort[i]>list_sort[i+1]:
                temp = list_sort[i]
                list_sort[i] = list_sort[i+1]
                list_sort[i+1] = temp
    return list_sort

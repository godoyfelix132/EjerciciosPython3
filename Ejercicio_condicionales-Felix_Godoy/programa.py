from paquete.funciones import *

#Funciones con un numero
print("Dame un numero: ")
n = int(input())
print("El numero", n, "es", type_num(n))
print("El numero", n, "es", even_odd(n))
print("El numero", n, prime(n))

#Funciones con un año
print("Dame un año: ")
a = int(input())
print("El año", a, leap_year(a))

#Funciones con una lista
list_num = [1, 2, 4, 1, 3]
list_sort = sort_list(list_num)
print(list_sort)



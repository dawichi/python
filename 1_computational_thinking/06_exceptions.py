''' Excepcion de errores
En este ejemplo, si pasamos un 0, caeremos en el ZeroDivisionError en la excepción y así no fallará el programa
'''
def divide_list_elements(list, divisor):
    try:
        return [i / divisor for i in list]
    except ZeroDivisionError as e:
        print(e)
        return list


list = list(range(10))
divisor = 0

print(divide_list_elements(list, divisor))
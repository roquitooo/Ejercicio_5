from banking_utils import consult_balance,insert_money,extract_money
from autentication_utils import user_autentication

def pedir_numero():
    while True: 
        try:
            argumento = float(input("\tEscribe un numero: "))
            return argumento
        except ValueError:
            print("No ingresaste un numero")

def menu():
    while True:
        menu = """
    Banco
    1.   Consultar el saldo
    2.   Ingresar dinero
    3.   Retirar dinero
    4.   Salir

    Opcion: """

    
        opcion = input(menu)
        match opcion:
            case '1':
                consult_balance()
            case '2':
                insert_money(" ")
            case '3':
                extract_money(" ")
            case '4':
                print('Saliendo al inicio')
                return user_autentication()
            case _:
                print('\t\nOpcion incorrecta!')

balance = 50000

def consult_balance():
   global balance
   print (f"\n\tEl dinero total es: ${balance}")


def insert_money(monto):
    global balance
    try:
        monto = int(input("Ingrese el monto que desea ingresar: "))
        balance +=  monto
        print(f"El saldo ahora es: ${balance}")
    except ValueError:
        print("Por favor, ingresa una cantidad válida.")

def extract_money(retiro):
    global balance
    try:
        retiro = int(input("Ingrese una cantidad a retirar: "))
        balance -= retiro
        print (f"El balance ahora es de {balance}")
    except ValueError:
        print ("Porfavor, Ingresa una cantidad valida")
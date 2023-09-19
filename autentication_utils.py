user = 'user'
contra = '1234'

def user_autentication():
    for i in range(3):
        usuario = input('Ingrese el usuario: ')
        constrasena = input('Ingrese la contraseña: ')
        if usuario == user and constrasena == contra:
            print('\nUsuario y contraseña correctos!\n')
            return True
        else:
            print(f'\nUsuario y contraseña incorrectos, le quedan {2-i} intentanos\n')
    return False
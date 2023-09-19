from utils import menu
from autentication_utils import user_autentication

def main():
    if user_autentication():
        menu()
    else:
        print('Saliendo')

# buena practica
if __name__ == "__main__":
    main()


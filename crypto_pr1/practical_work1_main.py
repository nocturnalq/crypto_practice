from crypto_pr1 import slogan_cipher, polibian_square, trithemius_cipher, vigener_cipher, hill_cipher


def menu_bar():
    print("""
________________________________
    
    [1] Лозунговый шифр
    [2] Полибианский квадрат
    [3] Шифр Тритемия
    [4] Шифр Виженера
    [5] Шифр Хилла
    """)

    cipher_number = input("Выберите номер шифра:\n")

    if cipher_number == '1':
        try:
            slogan_cipher.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()
    if cipher_number == '2':
        try:
            polibian_square.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()
    if cipher_number == '3':
        try:
            trithemius_cipher.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()
    if cipher_number == '4':
        try:
            vigener_cipher.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()
    if cipher_number == '5':
        try:
            hill_cipher.main()
        except KeyboardInterrupt:
            print("Выход...")
            exit()


def main():
    menu_bar()

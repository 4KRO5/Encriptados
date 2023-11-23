from Cesar_Encrypted import cesar_encrypted_input
from Bifido_Encrypted import bifido_encrypted_input
from Vigenere_Encrypted import vigenere_encrypted_menu

options = {
    "1": lambda: cesar_encrypted_input(cryptography = True),
    "2": lambda: cesar_encrypted_input(cryptography = False),
    "3": lambda: bifido_encrypted_input(cryptography = True),
    "4": lambda: bifido_encrypted_input(cryptography = False),
    "5": lambda: vigenere_encrypted_menu(cryptography = True),
    "6": lambda: vigenere_encrypted_menu(cryptography = False),
    "0": lambda: print("Programa Finalizado.")
}

while True:
    print("╔════════════════════════════════════════════════╗\n" +
          "║            Seleccione una operación            ║\n" +
          "╠══════════════════════╦═════════════════════════╣\n" +
          "║ 1.- Cifrado César    ║ 2.- Descifrado César    ║\n" +
          "║ 3.- Cifrado Bífido   ║ 4.- Descifrado Bífido   ║\n" +
          "║ 5.- Cifrado Vigenere ║ 6.- Descifrado Vigenere ║\n" +
          "╠══════════════════════╩═════════════════════════╣\n" +
          "║ 0.- Salir                                      ║\n" +
          "╚════════════════════════════════════════════════╝")
    
    option = input("› Ingrese el número de la opción: ")

    if option in options:
        options[option]()
        
    if option == "0":
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
from Cesar_Encrypted import cesar_encrypted_input
from Bifido_Encrypted import bifido_encrypted_input
# from Vigenere_Encrypted import vigenere_encrypted_input

options = {
    "1": lambda: cesar_encrypted_input(cryptography = True),
    "2": lambda: cesar_encrypted_input(cryptography = False),
    "3": lambda: bifido_encrypted_input(cryptography = True),
    "4": lambda: bifido_encrypted_input(cryptography = False),
    # "5": lambda: vigenere_encrypted_input(cifrar = True),
    # "6": lambda: vigenere_encrypted_input(cifrar = False),
    "0": lambda: print("Saliendo del programa.")
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

    if option == "0":
        break

    if option in options:
        options[option]()
    else:
        print("Opción no válida. Inténtelo de nuevo.")
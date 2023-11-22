# ///////////////////////////////////////// Input Cifrado Vigenere /////////////////////////////////////////
# def cifrado_Vigenere():
#     considerar_n = input("¿Desea considerar la letra 'Ñ' en el universo? (Sí: 1, No: 0): ")
    
#     while True:
#         palabra_original = input("Ingrese la palabra a cifrar: ")
#         if validar_clave_excepción(palabra_original):
#             break
        
#     while True:
#         clave_vigenere = input("Ingrese la clave Vigenere: ")
#         if validar_clave(clave_vigenere):
#             break
    
#     if considerar_n == "1":
#         palabra_cifrada_vigenere = cifrar_vigenere(palabra_original, clave_vigenere, considerar_n=True)
#     else:
#         palabra_cifrada_vigenere = cifrar_vigenere(palabra_original, clave_vigenere, considerar_n=False)

#     print("\n============= Resultado ===============\n" +
#          f"Palabra Original: {palabra_original}\n" +
#          f"Palabra Descifrada: {palabra_cifrada_vigenere}")

# def descifrado_Vigenere():
#     palabra_original = input("Ingrese la palabra a descifrar: ")
#     clave_vigenere = input("Ingrese la clave Vigenere: ")
#     considerar_n = input("¿Desea considerar la letra 'Ñ' en el universo? (Sí: 1, No: 0): ")

#     if considerar_n == "1":
#         palabra_descifrada_vigenere = descifrar_vigenere(palabra_original, clave_vigenere, considerar_n=True)
#     else:
#         palabra_descifrada_vigenere = descifrar_vigenere(palabra_original, clave_vigenere, considerar_n=False)

#     print("\n============= Resultado ===============\n" +
#          f"Palabra Original: {palabra_original}\n" +
#          f"Palabra Descifrada: {palabra_descifrada_vigenere}\n")

# ///////////////////////////////////////// Menu /////////////////////////////////////////
# def vigenere_encrypted_input():
#     options = {
#         # "1": lambda: universo_A_to_E(cifrar = True),
#         # "2": lambda: Universo_A_to_Z(cifrar = False),
#         # "3": lambda: user_defined_universe(cifrar = True),
#     }

#     while True:
#         print("╔════════════════════════════════════════════════╗\n" +
#               "║            Seleccione una operación            ║\n" +
#               "╠═══════════════════════╦════════════════════════╣\n" +
#               "║ 1.- Universo (A-E)    ║ 2.- Universo (A-Z)     ║\n" +
#               "║ 3.- Definir Universo  ║                        ║\n" +
#               "╚═══════════════════════╩════════════════════════╝")
        
#         option = input("› Ingrese el número de la opción: ")

#         if option == "0":
#             break

#         if option in options:
#             options[option]()
#         else:
#             print("Opción no válida. Inténtelo de nuevo.")
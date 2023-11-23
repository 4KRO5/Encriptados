def validate_input(word, isUniverse):
    if not all(c.isalpha() or c.isspace() for c in word.upper()):
        if isUniverse:
            print("╔══════════════════════════════════════════════╗\n" +
                  "║ Error: La palabra debe contener solo letras. ║\n" +
                  "║ Por favor, ingrese una palabra válida.       ║\n" +
                  "╚══════════════════════════════════════════════╝")
        else:
            print("╔═══════════════════════════════════════════════╗\n" +
                  "║ Error: El universo debe contener solo letras. ║\n" +
                  "║ Por favor, ingrese una palabra válida.        ║\n" +
                  "╚═══════════════════════════════════════════════╝")
        return False
    return True

def validate_input_exception(word):
    if not all(c.isalpha() or c.isspace() for c in word.upper()) or 'Ñ' in word.upper():
        print("╔═════════════════════════════════════════════════════════════════════════════╗\n" + 
              "║ Error: La palabra debe contener solo letras y no debe incluir la letra 'Ñ'. ║\n" +
              "║ Por favor, ingrese una palabra válida.                                      ║\n" +
              "╚═════════════════════════════════════════════════════════════════════════════╝")
        return False
    return True

def validate_input_universe(word, universe):
    if not all(c in universe.upper() or c.isspace() for c in word.upper()):
        print("╔════════════════════════════════════════════════════════════════════════╗\n" + 
              "║ Error: La palabra debe contener solo letras del universo seleccionado. ║\n" +
              "║ Por favor, ingrese una palabra válida.                                 ║\n" +
              "╚════════════════════════════════════════════════════════════════════════╝")
        return False
    return True

def validate_position(position):
    if not str(position).isdigit() or (str(position).isdigit() and int(position) < 0):
        print("╔════════════════════════════════════════════════════════════════════════╗\n" + 
              "║ Error: La posición debe ser un valor numérico positivo diferente de 0. ║\n" +
              "║ Por favor, ingrese una posición válida.                                ║\n" +
              "╚════════════════════════════════════════════════════════════════════════╝")
        return False
    return True
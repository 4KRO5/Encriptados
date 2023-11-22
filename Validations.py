def validate_input(word):
    if not all(c.isalpha() or c.isspace() for c in word.upper()):
        print("╔══════════════════════════════════════════════╗\n" +
              "║ Error: La palabra debe contener solo letras. ║\n" +
              "║ Por favor, ingrese una palabra válida.       ║\n" +
              "╚══════════════════════════════════════════════╝")
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
    if not all(c.isalpha() or c.isspace() and c in universe.upper() for c in word.upper()):
        print("╔════════════════════════════════════════════════════════════════════════╗\n" + 
              "║ Error: La palabra debe contener solo letras del universo seleccionado. ║\n" +
              "║ Por favor, ingrese una palabra válida.                                 ║\n" +
              "╚════════════════════════════════════════════════════════════════════════╝")
        return False
    return True

def validate_position(position):
    if not str(position).isdigit() or int(position) < 0:
        print("╔════════════════════════════════════════════════════════════════════════╗\n" + 
              "║ Error: La posición debe ser un valor numérico positivo diferente de 0. ║\n" +
              "║ Por favor, ingrese una posición válida.                                ║\n" +
              "╚════════════════════════════════════════════════════════════════════════╝")
        return False
    return True
# Jose Alfonzo 17-10012 
# Pregunta 2)


# Funcion que recibe un operador y dos operandos. Retorna el resultado de la operacion.
def evaluar(operador: str,opIzquierdo: str,opDerecho: str) -> int:
    # Sumas
    if operador == "+":
        return int(opIzquierdo)+int(opDerecho)
    # Restas
    elif operador == "-":
        return int(opIzquierdo)-int(opDerecho)
    # Multiplicaciones
    elif operador == "*":
        return int(opIzquierdo)*int(opDerecho)
    # Divisiones
    elif operador == "/":
        return int(opIzquierdo)//int(opDerecho)

# Funcion que recibe un operador y dos operandos. Retorna la expresion en notacion infija.
def mostrar(operador: str,opIzquierdo: str,opDerecho: str) -> str:
    # Comprobamos si el operador es + -
    if operador in "+-":
        if len(opDerecho) == 2 and int(opDerecho) < 0:
            opDerecho = f"({opDerecho})"
        return opIzquierdo + " " + operador + " " + opDerecho
    # Comprobamos si el operador es * /
    elif operador in "*/":
        if len(opIzquierdo) > 1:
            opIzquierdo = f"({opIzquierdo})"
        if len(opDerecho) > 1:
            opDerecho = f"({opDerecho})"
        return opIzquierdo + " " + operador + " " + opDerecho
       
# Funcion que recibe una expresion en orden prefijo.Retorna la expresion evaluada.
def prefijo(accion: str,expresion: list) -> str:
    # Creamos una lista vacia
    stack = []
    # Recorremos la expresion en orden prefijo, es decir de derecha a izquierda
    for i in range(len(expresion)-1,-1,-1):
        # Vemos si el caracter es un operador para obtener el operador y los operandos
        if expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "*" or expresion[i] == "/":
            opIzquierdo = stack.pop()
            opDerecho = stack.pop()
            operador = expresion[i]
            # Dependiendo de cual sea la accion,calculamos su resultado correspondiente y lo metemos en la pila
            if accion == "EVAL":
                resultado = evaluar(operador, opIzquierdo, opDerecho)
            elif accion == "MOSTRAR":    
                resultado = mostrar(operador, opIzquierdo, opDerecho)

            stack.append(f"{resultado}")
        # Vemos si caracter es un operando y lo metemos en la pila
        else:
            stack.append(expresion[i])
    return stack[0]

# Funcion en orden postfijo. Retorna la evaluacion de la expresion.
def postfijo(accion: str,expresion: list) -> str:
    # Creamos una lista vacia
    stack = []
    # Recorremos la expresion en orden prefijo, es decir de izquierda a derecha
    for i in range(0, len(expresion)):
        # Vemos si el caracter es un operador para obtener el operador y los operandos
        if expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "*" or expresion[i] == "/":
            opDerecho = stack.pop()
            opIzquierdo = stack.pop()
            operador = expresion[i]
            # Dependiendo de cual sea la accion,calculamos su resultado correspondiente y lo metemos en la pila
            if accion == "EVAL":    
                resultado = evaluar(operador, opIzquierdo, opDerecho)
            elif accion == "MOSTRAR":    
                resultado = mostrar(operador, opIzquierdo, opDerecho)
            stack.append(f"{resultado}")
        # Vemos si caracter es un operando y lo metemos en la pila
        else:
            # insertar el operando en la stack:
            stack.append(expresion[i])
    return stack[0]

# Funcion principal que procesa la entrada del usuario y ejecuta todo de acuerdo al enunciado del ejercicio
def procesar(accion: str) -> str:
    accion = accion.strip().split()
    # Dependiendo de cada accion que nos de el usuario, pedimos los parametros
    # En este caso pedimos <orden> y <expr>  
    if accion[0] == "EVAL":
        try:
            orden = accion[1]
        except:
            return "Falta el parametro <orden>"
        if orden != "PRE" and orden != "POST": 
            return "El orden no valido, tiene que ser PRE o POST"
        # Guardamos la expresion
        expr = accion[2:]
        if not expr:
            return "Falta el parametro <expr>"
        # Si el orden es PRE usamos prefijo() y devolvemos el resultado
        if orden == "PRE":
            resultado = prefijo("EVAL", expr)
            return resultado
        # Si el orden es POST usamos postfijo() y devolvemos el resultado
        elif orden == "POST":
            resultado = postfijo("EVAL", expr)
            return resultado
    # En este caso pedimos <orden> y <expr> tambien
    elif accion[0] == "MOSTRAR":
        try:
            orden = accion[1]
        except:
            return "Falta el parametro <orden>"
        if orden != "PRE" and orden != "POST": 
            return "El orden no valido, tiene que ser PRE o POST"
        # Guardamos la expresion
        expr = accion[2:]
        if not expr:
            return "Falta el parametro <expr>"

        # Si el orden es PRE usamos prefijo() y devolvemos el resultado
        if orden == "PRE":
            resultado = prefijo("MOSTRAR", expr)
            return resultado

        # Si el orden es POST usamos postfijo() y devolvemos el resultado
        elif orden == "POST":
            resultado = postfijo("MOSTRAR", expr)
            return resultado        

    # Si el usuario ingresa SALIR entonces:
    elif accion[0] == "SALIR":
        # Se termina el programa
        exit()
    else:
        return "La accion no es ni EVAL,MOSTRAR o SALIR"


if __name__ == "__main__":
    # Pedimos al usuario que ingrese una accion hasta que esta sea SALIR
    while True:
        accion = input("Ingrese una accion:\nEVAL <orden> <expr>\nMOSTRAR <orden> <expr>\nSALIR\n\n")
        resultado = procesar(accion)
        # Mostramos el resultado
        print(f"{resultado}\n")
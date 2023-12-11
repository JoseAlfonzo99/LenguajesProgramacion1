# Jose Alfonzo 17-10012

from Pregunta4 import *
manejador = ManejadorTablas()

# Funcion que se creo para simplificar los test en el archivo Test.py 
def simplificar(accion: str) -> str:
    # Atrapamos la accion del usuario
    accion = accion.strip().split()
    # Determinamos cual accion igreso el usuario y si es valida
    if accion:
        if accion[0] == "CLASS":
            msj = manejador.definir(accion[1:])
        elif accion[0] == "DESCRIBIR":
            msj = manejador.describir(accion[1:])
        elif accion[0] == "SALIR":
            exit()
        else:
            msj = "Accion invalida, debe ser una de las siguientes: 'CLASS' 'DESCRIBIR' 'SALIR'"
    else:
        msj = "No se ingreso ninguna accion"
    return msj
# Main
if __name__ == "__main__":
    print(" Bienvenido al manejador de tablas de metodos virtuales")
    while True:
        #print("\nIngrese una accion:\nCLASS <tipo> [<nombre>]\nDESCRIBIR <nombre> <expr>\nSALIR\n\n")
        accion = input("Ingrese una de las siguientes acciones: 'CLASS' 'DESCRIBIR' 'SALIR'\n")
        respuesta = simplificar(accion)
        if not respuesta.startswith("Clase"):
            print(f"{respuesta}")
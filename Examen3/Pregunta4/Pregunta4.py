# Jose Alfonzo 17-10012

class Clase:
    def __init__(self, nombreClase: str, metodos: list, padre = None):
        # Constructor
        self.nombreClase = nombreClase
        self.padre = padre
        self.metodosFinales = {}
        if isinstance(padre, Clase):
            self.metodosFinales = padre.metodosFinales.copy()
        # Iteramos en nustros metodos
        for i in metodos:
            self.metodosFinales[i] = nombreClase

class ManejadorTablas:
    def __init__(self) -> None:
        # Diccionario que contiene los tipos de clases y sus metodos
        self.tabla = {}
    # Funcion que define una nueva clase
    def definir(self, accion: list) -> str:
        hijo = accion[0]
        #  si el nombre de la nueva clase ya existe no se vuelve a colocar
        if hijo not in self.tabla:
            # Si tiene : el nombre, significa que viene con herencia
            if accion[1] == ":":
                superPadre = accion[2]
                if superPadre in self.tabla:
                    clasePapa = self.tabla[superPadre]
                    metodosDeHijo = accion[3:]
                else:
                    return f"La clase {superPadre} no existe"
            # Si no tiene : significa que no tiene herencia
            else:
                clasePapa = None
                metodosDeHijo = accion[1:]
            auxLista = [x for x in metodosDeHijo if metodosDeHijo.count(x) <= 1]
            # Verificamos si los metodos se llaman igual
            if len(auxLista) < len(metodosDeHijo):
                return f"Hay definiciones repetidas en la lista de nombres de metodos"
            # Creamos un nuevo hijo
            claseHijoNuevo = Clase(hijo, metodosDeHijo, clasePapa)
            self.tabla[hijo] = claseHijoNuevo
            return f"Clase {hijo} con los metodos {claseHijoNuevo.metodosFinales}"
        else:
            return f"El nombre de la nueva clase: {hijo} :ya existe"
    # Funcion que describe una clase especificada 
    def describir(self, accion: str) -> str:
        # Mostramos la descripcion de la clase de acuerdo al enunciado
        if accion[0] in self.tabla:
            clase = self.tabla[accion[0]]
            metodosClase = clase.metodosFinales.copy()
            descripcion = '\n'.join([f'{metodo} -> {metodosClase[metodo]} :: {metodo}' for metodo in metodosClase.keys()])
            return descripcion
        else:
            return f"La clase {accion[0]} no existe"
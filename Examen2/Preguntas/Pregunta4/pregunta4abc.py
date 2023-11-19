# Jose Alfonzo 17-10012 
# Pregunta 4)


# Funcion F
# F_{alpha,beta}(n) = n                                                                                           si 0 <= n < alpha*beta
#                   = F_{alpha,beta}(n-beta*1) + F_{alpha,beta}(n-beta*2) + ... + F_{alpha,beta}(n-beta*alpha)    si n >= alpha*beta

# Tomando como referencia las constantes X, Y, Z, del carnet, tenemos que
# X = 0 
# Y = 1 
# Z = 2

# alpha = ((0 + 1) mod 5) + 3 = (1 mod 5) + 3 = 4
# beta = ((1 + 2) mod 5) + 3 = (3 mod 5) + 3 = 6

# Por lo tanto 

# F_{4,6}(n) = n                                                      si 0 <= n < 4*6
#            = F_{4,6}(n-6*1) + F_{4,6}(n-6*2) +...+ F_{4,6}(n-6*4)   si n >= 4*6

# Entonces nos queda

# F_{4,3}(n) = n                                                  si 0 <= n < 24
#            = F_{4,6}(n-6) + F_{4,6}(n-12) +...+ F_{4,6}(n-24)   si n >= 24


import time
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# a) Funcion Recursiva para los valores de alpha= 4 y beta = 6
def funcionRecursiva(n: int) -> int:
    # Escribimos el codigo de la funcion que nos queda en la linea 25
    # Casos base
    if 0 <= n < 24:
        return n
    # Casos no base
    elif n >= 24:
        return funcionRecursiva(n-6*1) + funcionRecursiva(n-6*2) + funcionRecursiva(n-6*3) + funcionRecursiva(n-6*4)

# b) Funcion Recursiva de cola para los valores de alpha= 4 y beta = 6
def funcionRecursivaCola(n: int, aux: list, i=0) -> int:
    # Casos base
    if 0 <= n < 24:
        return aux[n+i]
    # Casos no base
    elif n >= 24:
        aux.append(aux[18+i]+aux[12+i]+aux[6+i]+aux[0+i])   
        return funcionRecursivaCola(n- 1, aux, i+1)

# c) Funcion iterativa proveniente de la recursion de cola para los valores de alpha= 4 y beta = 6
def funcionIterativa(n: int) -> int:
    # Creamos nuestra sucesion
    aux = [i for i in range(24)]
    # Casos base:
    if 0 <= n < 24:
        return n
    # Casos no base
    elif n >= 24:
        i = 0       
        # Metemos los valores de la sucesion correspondientes a 24 hasta n
        for k in range(24, n+1):
            aux.append(aux[18+i]+aux[12+i]+aux[6+i]+aux[0+i])
            i = i + 1
        return aux[len(aux)-1]

# Comparamos las funciones de recursion,recursion de cola e iterativa 
if '__main__' == __name__:
    # Creamos las variables a utilizar
    numFinal = int(input("Ingrese el nro final de n: "))
    numPasos = int(input(f"Ingrese el nro pasos desde 0 hasta {numFinal}: "))
    valores = [i for i in range(0, numFinal+numPasos, numPasos)]
    # Arreglos de tuplas  que guardaran los tiempos de ejecucion y sus resultados
    resultadosRecursiva = []
    resultadosRecursivaCola = []
    resultadosIterativa = []

    for n in valores:
        # Funcion Recursiva
        tiempo_inicial = time.time()
        resultado = funcionRecursiva(n)
        tiempo_final = time.time()
        resultadosRecursiva.append((resultado, tiempo_final - tiempo_inicial))
        # Funcion Recursiva de cola
        listaalphabeta = [i for i in range(24)]
        tiempo_inicial = time.time()
        resultado = funcionRecursivaCola(n, listaalphabeta)
        tiempo_final = time.time()
        resultadosRecursivaCola.append((resultado, tiempo_final - tiempo_inicial))
        # Funcion Iterativa
        tiempo_inicial = time.time()
        resultado = funcionIterativa(n)
        tiempo_final = time.time()
        resultadosIterativa.append((resultado, tiempo_final - tiempo_inicial))

    # Imprimimos los resultados
    print(f"\nResultados de la ejecucion:")
    print(f"*******************************************************************************")
    print(f"n \t\t| Recursiva \t\t| Recursiva Cola \t| Iterativo")
    print(f"*******************************************************************************")
    for i in range(len(valores)):
        if resultadosRecursiva[i][0] < 10000:
            print(f"{valores[i]} \t\t| {resultadosRecursiva[i][0]} \t\t\t| {resultadosRecursivaCola[i][0]} \t\t\t| {resultadosIterativa[i][0]}")
        else:
            print(f"{valores[i]} \t\t| {resultadosRecursiva[i][0]} \t\t| {resultadosRecursivaCola[i][0]} \t\t| {resultadosIterativa[i][0]}")

    print(f"\n\nSegundos de los tiempos de ejecucion:")
    print(f"*******************************************************************************")
    print(f"n \t\t| Recursiva \t\t| Recursiva Cola \t| Iterativo")
    print(f"*******************************************************************************")
    for i in range(len(valores)):
        print(f"{valores[i]} \t\t| {resultadosRecursiva[i][1]:.5f} \t\t| {resultadosRecursivaCola[i][1]:.5f} \t\t| {resultadosIterativa[i][1]:.5f}")

    # Graficamos los resultados utilizando plot
    plt.plot(valores, [i[1] for i in resultadosRecursiva], label="Recursiva")
    plt.plot(valores, [i[1] for i in resultadosRecursivaCola], label="Recursiva Cola")
    plt.plot(valores, [i[1] for i in resultadosIterativa], label="Iterativo")
    plt.xlabel("Valores de n")
    plt.ylabel("Segundos")
    plt.title(" Grafico con los Tiempos de Resultados de Ejecucion")
    plt.legend()
    plt.show()

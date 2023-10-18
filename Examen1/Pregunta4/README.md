# Jose Alfonzo 17-10012
# Pasos para ejecutar Pregunta4 del examen 1

Nota: Se utilizo un sistema operativo Linux con el compilador g++ ya intalado

1) Abra la terminal
2) Instale la libreria gcovr con el siguiente comando:
``` sudo apt install gcovr ```
3) En caso que ya la instale, puede revisarlo usando el siguiente comando:
``` gcovr --version```
4) Compilar el programa con los siguientes comandos:
``` g++ --coverage -c -o Pregunta4.o Pregunta4.cpp  ```

``` g++ --coverage -c -o Pregunta4Test.o Pregunta4Test.cpp ```

``` g++ --coverage -o ejecutable Pregunta4.o Pregunta4Test.o ```

5) Ejecutar el programa con el siguiente comando:
``` ./ejecutable ```



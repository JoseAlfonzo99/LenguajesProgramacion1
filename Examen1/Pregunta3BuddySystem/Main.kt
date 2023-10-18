
// Jose Alfonzo 17-10012 Main de la Pregunta 3 

import Pregunta3
fun main(args: Array<String>) {
    // Creamos el buddy System
    val buddySystem = Pregunta3(args[0].toInt())
    // Leemos los datos de entrada
    while (true) {
        println("Desea RESERVAR-LIBERAR-MOSTRAR-SALIR? ")
        print("> ")
        var entrada = readLine()!!.split(" ")
        if (entrada.size > 3 || entrada.size < 1) {
            println("No se ingresaron de manera correcta los datos")
        } else if (entrada[0] != "SALIR" && entrada[0] != "RESERVAR" && entrada[0] != "LIBERAR" && entrada[0] != "MOSTRAR") {
            println("No se ingresaron de manera correcta los datos")
        } else {
            when (entrada[0]){
                // Abortamos la ejecucion cuando se reciba la palabra SALIR
                "SALIR" -> {break}
                "RESERVAR" -> try {
                    if (entrada.size != 3) {
                        println("No se ingresaron de manera correcta los datos al usar RESERVAR")
                    } else if (entrada[1].toInt() < 0) {
                        println("No se ingresaron de manera correcta los datos al usar RESERVAR")
                    } else if (entrada[1].toInt() > args[0].toInt()) {
                        println("No hay un espacio libre suficientemente grande como para satisfacer la petición")
                    } else {
                        // Llamamos nuestro metodo para reservar los bloques que el usuario nos indique
                        buddySystem.reservar(entrada[1].toInt(), entrada[2])
                    }
                } catch(e: NumberFormatException) { println("No se ingresaron de manera correcta los datos al usar RESERVAR")}
                "LIBERAR" -> {
                    if (entrada.size != 2) {
                        println("No se ingresaron de manera correcta los datos al usar LIBERAR debe tener un parametro")
                    } else {
                        // Llamamos nuestro metodo para liberar los bloques que el usuario nos indique
                        buddySystem.liberar(entrada[1])
                    }
                }
                "MOSTRAR" -> {
                    // Llamamos nuestro metodo para mostrar los bloques
                    buddySystem.mostrar()
                }
            }
        }
    }
}

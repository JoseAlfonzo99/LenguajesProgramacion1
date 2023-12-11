// Jose Alfonzo 17-10012

import java.util.LinkedList

// Clase abstracta que representa una secuencia
abstract class Secuencia<T> {

    // Funcion que agrega un elemento a la secuencia
    abstract fun agregar(e: T)

    // Funcion que remueve un elemento a la secuencia y lo devuelve
    abstract fun remover() : T

    // Funcion que verifica si la secuencia esta o no vacia
    abstract fun vacio() : Boolean
}

// Clase que funciona como una Pila y es subtipo de Secuencia (hereda de secuencia)
class Pila<T> : Secuencia<T>() {
    private var pila : LinkedList<T> = LinkedList<T>()
    
    // Funcion que empila un elemento a la pila
    override fun agregar(e: T) { 
        pila.add(e) 
    }
    
    // Funcion que remueve un elemento de la pila y devuelve un error si la pila ya esta vacia
    override fun remover() : T {
        if (vacio()) { throw RuntimeException("Error: Ya esta vacia la pila") }
         return pila.removeLast()
    }
    
    // Funcion que determina si la pila esta vacia
    override fun vacio() : Boolean = (pila.size == 0)
}

// Clase que funciona como una Cola y es subtipo de Secuencia (hereda de secuencia)
class Cola<T> : Secuencia<T>() {
    private var cola : LinkedList<T> = LinkedList<T>()
    
    // Funcion que encola un elemento a la cola
    override fun agregar(e: T) { cola.add(e) }
    
    // Funcion que desencola un elemento de la cola y devuelve un error si la cola ya esta vacia
    override fun remover() : T {
        if (vacio()) { throw RuntimeException("Error: Ya esta vacia la cola") }
        return cola.removeFirst()
    }
    // Funcion que determina si la cola esta vacia
    override fun vacio() : Boolean = (cola.size == 0)
}

// Clase que representa grafos
class Grafo {
    private val adyacencias: MutableMap<Int, MutableList<Int>> = mutableMapOf()
    fun agregarVertice(vertice: Int) {
        adyacencias[vertice] = mutableListOf()
    }
    fun agregarArista(origen: Int, destino: Int) {
        adyacencias[origen]?.add(destino)
    }
    fun obtenerAdyacencias(vertice: Int): List<Int>? {
        return adyacencias[vertice]
    }
}

// Clase abstracta Busqueda para buscar nodos
abstract class Busqueda {
    abstract fun buscar(grafo: Grafo, inicio: Int, objetivo: Int): Int
}

// Clase DFS 
class DFS : Busqueda() {
    override fun buscar(grafo: Grafo, inicio: Int, objetivo: Int): Int {
        // Creamos las variables
        val visitados = mutableSetOf<Int>()
        val pila = Pila<Int>()
        var nodosExplorados = 0
        pila.agregar(inicio)
        while (!pila.vacio()) {
            val actual = pila.remover()
            if (actual == objetivo) {
                return nodosExplorados
            }
            if (actual !in visitados) {
                visitados.add(actual)
                nodosExplorados++
                grafo.obtenerAdyacencias(actual)?.reversed()?.forEach {
                    if (it !in visitados) {
                        pila.agregar(it)
                    }
                }
            }
        }
        return -1
    }
}

// Clase BFS que implementa la búsqueda a amplitud
class BFS : Busqueda() {
    override fun buscar(grafo: Grafo, inicio: Int, objetivo: Int): Int {
        // Creamos las variables
        val visitados = mutableSetOf<Int>()
        val cola = Cola<Int>()
        var nodosExplorados = 0
        cola.agregar(inicio)
        while (!cola.vacio()) {
            val actual = cola.remover()
            if (actual == objetivo) {
                return nodosExplorados
            }
            if (actual !in visitados) {
                visitados.add(actual)
                nodosExplorados++
                grafo.obtenerAdyacencias(actual)?.forEach {
                    if (it !in visitados) {
                        cola.agregar(it)
                    }
                }
            }
        }
        return -1
    }
}
// Funcion principal
fun main() {
    // variables que tendran una pila y una cola
    val pila = Pila<Int>()
    val cola = Cola<Int>()
    // Agregamos elementos a la pila
    pila.agregar(1)
    pila.agregar(2)
    pila.agregar(3)
    // Agregamos elementos a la cola
    cola.agregar(1)
    cola.agregar(2)
    cola.agregar(3)
    // Removemos elementos de la pila
    println("Elementos de la pila:")
    while (!pila.vacio()) {
        println(pila.remover())
    }
    // Removemos elementos de la cola
    println("Elementos de la cola:")
    while (!cola.vacio()) {
        println(cola.remover())
    }
    val grafo = Grafo()
    grafo.agregarVertice(0)
    grafo.agregarVertice(1)
    grafo.agregarVertice(2)
    grafo.agregarVertice(3)
    grafo.agregarArista(0, 1)
    grafo.agregarArista(1, 3)
    grafo.agregarArista(0, 2)
    val busquedaBFS = BFS()
    val respuestaBFS = busquedaBFS.buscar(grafo, 2, 3)
    println("Recorrido con BFS y los nodos explorados: $respuestaBFS")
    val busquedaDFS = DFS()
    val respuestaDFS = busquedaDFS.buscar(grafo, 0, 1)
    println("Recorrido con DFS y los nodos explorados: $respuestaDFS")
}


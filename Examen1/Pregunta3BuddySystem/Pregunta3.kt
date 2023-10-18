
// Jose Alfonzo 17-10012

public class Pregunta3 {
    // Variables de la clase
    // Tamano de memoria
    private var size: Int;
    // Listas de bloques libres
    private var bloqueLibres: MutableList<MutableList<Pair<Int, Int>>>;
    // Almacena los espacios de memoria
    private var bloquesLlenos: HashMap<String,Pair<Int, Int>> = HashMap<String,Pair<Int, Int>>()
    // Constructor
    constructor(s: Int) {
        size = s;
        // Posibles potencias de 2
        val x = Math.ceil(Math.log(size.toDouble()) / Math.log(2.0)).toInt();
        bloqueLibres = MutableList(x+1, {mutableListOf()});
        bloqueLibres[x].add(Pair(0, size - 1)); 
    }    

    // Metodo para reservar la memoria
    fun reservar(cantidad: Int,nombre: String): Boolean {

        if (bloquesLlenos.containsKey(nombre)) {
            println("${nombre} ya tiene memoria reservada")
            return false
        }
        
        val x = Math.ceil(Math.log(cantidad.toDouble()) / Math.log(2.0)).toInt();
        var i: Int;
        var aux: Pair<Int, Int>;

        // Buscamos un bloque donde se pueda colocar
        if (bloqueLibres[x].size > 0) {
            // Actualizamos el valor de aux
            aux = bloqueLibres[x].removeAt(0);
            bloquesLlenos.put(nombre, aux);
            return true;
        }
        i = x + 1
        while (i < bloqueLibres.size) {
            if (bloqueLibres[i].size == 0) {
                i = i + 1
                continue;
            }           
            break; 
        }
        
        if (i == bloqueLibres.size) {
            println("no hay un espacio libre contiguo suficientemente grande como para satisfacer la petición")
            return false
        }
        
        // Borramos el primer bloque
        aux = bloqueLibres[i].removeAt(0);
        i--;
        while (i >= x) {
            // Creamos dos tuplas
            var tupla: Pair<Int, Int> = Pair(aux.first, aux.first +(aux.second - aux.first) /2); 
            var tupla2: Pair<Int, Int> = Pair(aux.first +(aux.second - aux.first + 1) /2, aux.second); 
            bloqueLibres[i].add(tupla);
            bloqueLibres[i].add(tupla2);
            aux = bloqueLibres[i].removeAt(0);
            i = i - 1
        }
        bloquesLlenos.put(nombre, aux);
        return true;

    }

    // Metodo para liberar memoria
    fun liberar(nombre: String) : Boolean {

        // verificar que el nombre tenga un espacio de memoria asignado
        if (!bloquesLlenos.containsKey(nombre)) {
            println("${nombre} no tiene memoria reservada")
            return false
        }
        // Inicializamos las variables a usar
        var bloqueParaBorrar = bloquesLlenos.get(nombre)
        var s= bloqueParaBorrar!!.first
        var espacio= espacio(bloqueParaBorrar)
        var x = Math.ceil(Math.log(espacio.toDouble())/Math.log(2.0)).toInt()
        var i: Int;
        // Numero Buddy System
        var numeroBS: Int;
        // Direccion Buddy System
        var direccionBS: Int;
        bloqueLibres[x].add(bloqueParaBorrar)
        // Operamos numero BS
        numeroBS= s/espacio
        if (numeroBS % 2 != 0) {
            direccionBS= s -(Math.pow(2.0, x.toDouble())).toInt();
        } else {
            direccionBS= s +(Math.pow(2.0, x.toDouble())).toInt();
        }
        i = 0
        while (i < bloqueLibres[x].size) {
            // Vemos si el bloque contiguo esta sin ser llenado
            if (bloqueLibres[x][i].first == direccionBS) {
                if (numeroBS % 2 ==0) {
                    // Lo metemos en su lista correspondiente
                    bloqueLibres[x+1].add(Pair(s,s+ 2*(Math.pow(2.0, x.toDouble())).toInt() - 1));

                } else {
                    // Lo metemos en su lista correspondiente
                    bloqueLibres[x + 1].add(Pair(direccionBS,direccionBS+ 2 *(Math.pow(2.0, x.toDouble())).toInt() - 1));
                }
                // Borramos apropiadamente
                bloqueLibres[x].removeAt(i);
                bloqueLibres[x].removeAt(bloqueLibres[x].size- 1);
                break;
            }
            i++
        }
        // Liberamos el bloque
        bloquesLlenos.remove(nombre)
        return true
    }

    // Metodo que nos muestra informacion de los bloque de cada nombre y los bloques libres
    fun mostrar() {
        println("Las listas de bloques libres son :")
        println("${bloqueLibres} \n")
        for(key in bloquesLlenos.keys){  
            println("El bloque de memoria de ${key} es ${bloquesLlenos[key]}")  
        }
    }
}
// Calcula los bytes de un bloque de memoria
fun espacio(bloque: Pair<Int, Int>) : Int {
    return bloque.second - bloque.first + 1
}
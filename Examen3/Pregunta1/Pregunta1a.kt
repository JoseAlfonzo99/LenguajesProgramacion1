// Jose Alfonzo 17-10012


class Calculadora(var a: Int,var b: Int) {
    fun suma() : Int = a + b
}
class Letras {
    public var publico: String = "publico"
    private var privado: String = "privado"
    protected var protegido: String = "protegido"
    internal var interno: String = "interno"
}
interface Algo<in T> {
    fun algo (algo1: T, algo2: T): Int
}
interface List<out A> {
    fun get(): List<A>
}

fun main() {
    val ejemplo = Calculadora(1,2)
    println(ejemplo.suma())
}

// Jose Alfonzo 17-10012

/*
  parte iii de la pregunta 1)a)

*/

var variable1 = {valor: 5}
var variable2 = variable1 
// Imprime 5
console.log(variable2.valor)
// Modificamos el valor de la variable 1
variable1.valor = 4
// Imprime 4
console.log(variable2.valor)

var a = 1
var b = 2
// Imprime una suma cuyo resultado es 3
console.log(a + b)

a = 'Soy'
b = ' Jose'
// Imprime el string Soy Jose
console.log(a + b)


var polimorfismo = ['hay','polimorfismo']
// Imprime 2
console.log(polimorfismo.length)
var tambienAqui = [765,21]
// Imprime 2
console.log(tambienAqui.length)

//////// ejercicio de rotar 

function rotar(w,k) {
  if (k != 0) {
    for (var i =1; i <= k; i++) { 
      // Usamos las siguientes librerias para manipular el string,la primera me da el extring
      // sin el char indicado y la segunda me extrae el char indicado
      w = w.substr(1) + w.charAt(0)
    }
    return w
  } else {
    return w
  }
}
// Imprimir resultado
console.log(rotar('hola',1))
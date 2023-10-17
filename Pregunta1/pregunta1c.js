
// Jose Alfonzo 17-10012

///// Multiplicar una matriz con su traspuesta

var a = [[1,2],[3,4]]
var at = new Array(a.length)

// Llenamos la matriz at con 0 por los momentos
for (x = 0; x<at.length;x++){
    at[x] = new Array(a[0].length).fill(0);
} 
// Llenamos la matriz at con sus valores correctos
for (var i = 0; i<a.length;i++) {
    for (var j = 0; j<a[0].length;j++){
        at[i][j] = a[j][i]
    }
}

// Creamos nuvas variables
var fila_a = a.length
var columna_a = a[0].length
var fila_at = at.length
var columna_at = at[0].length

// Variable que guardara la respuesta
var multiplicacion = new Array(fila_a);
for (x = 0; x <multiplicacion.length;x++){
    multiplicacion[x] = new Array(columna_at).fill(0);
}
// Multiplicamos las matrices a y at  
for (x = 0; x < multiplicacion.length; x++) {
    for (y = 0; y < multiplicacion[x].length; y++) {                                
        for (z = 0; z<columna_a; z++) {
            multiplicacion [x][y] = multiplicacion [x][y] + a[x][z]*at[z][y] 
        }
    }
}
// Imprimir resultado
console.log(multiplicacion)

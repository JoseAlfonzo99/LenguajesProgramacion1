
// Jose Alfonzo 17-10012 Pregunta 4 tests de modulo


#include "Pregunta4.cpp"
using namespace std;
#include <cassert>

int main() {

    //Ejemplos
    Vector ejemploNulo;
    // Mostrar vector nulo
    cout << " ejemploNulo = ( " << ejemploNulo.a <<"," <<ejemploNulo.b << "," <<ejemploNulo.c << " )\n" << endl;

    Vector ejemplo1(5,7,88.2);
    // Mostrar ejemplo1
    cout << " ejemplo1 = ( " <<ejemplo1.a <<"," <<ejemplo1.b << "," <<ejemplo1.c << " )\n" << endl;

    Vector ejemplo2(25,9,7.1);
    // Mostrar ejemplo2
    cout << " ejemplo2 = ( " <<ejemplo2.a <<"," <<ejemplo2.b << "," <<ejemplo2.c << " )\n" << endl;

    Vector ejemplo3(-384, 11.8,-2);
    // Mostrar ejemplo3
    cout << " ejemplo3 = ( " <<ejemplo3.a <<"," <<ejemplo3.b << "," <<ejemplo3.c << " )\n" << endl;

    Vector ejemplo4(-16, 8 ,543);
    // Mostrar ejemplo4
    cout << " ejemplo4 = ( " <<ejemplo4.a <<"," <<ejemplo4.b << "," <<ejemplo4.c << " )\n" << endl;

    // A continuacion se probaran diversos casos de prueba

    // Caso 1
    Vector caso1 = ejemplo1 +ejemplo2;
    cout << " Caso 1: ejemplo1 + ejemplo2 = " <<caso1.a << " " <<caso1.b << " " <<caso1.c << "\n"<< endl;

    // Caso 2
    Vector caso2 = ejemplo4*ejemploNulo+ejemplo3;

    cout << " Caso2: ejemplo4 * ejemploNulo + ejemplo3 = " <<caso2.a << " " <<caso2.b<< " " <<caso2.c <<"\n"<< endl;

    // Caso 3

    Vector caso3 = (ejemplo2 + ejemplo4) *(ejemplo1);

    cout << " Caso3: (ejemplo2 + ejemplo4) * (ejemplo1) = " <<caso3.a << " " <<caso3.b << " " <<caso3.c << "\n"<< endl;

    // Caso 4

    Vector caso4 = ejemploNulo + 6;

    cout << " Caso4: ejemploNulo + 6 = " <<caso4.a << " " <<caso4.b << " " <<caso4.c << "\n"<< endl;

    // Caso 5

    double caso5 = & ejemplo3;
    cout << " Caso5: la norma del ejemplo3  = " <<caso5<< "\n"<< endl;

    // Caso 6

    double caso6 = ejemplo1 % (ejemplo3 * ejemplo2);
    cout << " Caso6: ejemplo1 % (ejemplo3 * ejemplo2) = " <<caso6<< "\n"<< endl;

    return 0;
}

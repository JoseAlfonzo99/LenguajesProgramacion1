
// Jose Alfonzo 17-10012 Pregunta 4 Implementacion de modulo

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

//Construimos un vector
class Vector {

public:
    double a,b,c;
    Vector(){
        this->a = 0;
        this->b = 0;
        this->c = 0;
    }

    Vector(double _x , double _y, double _z ): a(_x), b(_y), c(_z){}

        //Suma
        Vector operator+(const Vector v){return Vector(a + v.a, b + v.b, c + v.c);}

        //Resta
        Vector operator-(const Vector v){return Vector(a - v.a, b - v.b, c - v.c);}

         //Producto punto
        double operator%(Vector other){return (this-> a * other.a + this-> b * other.b + this->c * other.c);}

        // Producto cruz
        Vector operator*(const Vector v){return Vector(b *v.c - c*v.b, c*v.a - a*v.c, a*v.b - b *v.a);}

        // Operaciones con vectores
        Vector operator+(double aux){return Vector(a + aux, b + aux, c +aux);}

        Vector operator-(double aux){return Vector(a - aux, b -aux, c - aux);}

        Vector operator*(double aux){return Vector(a *aux, b *aux, c *aux);}
        // Norma
        double operator&(){return sqrt(a * a + b * b + c * c);}
};

-- Jose Alfonzo 17-10012 

---  pregunta 1)b)
with Ada.Text_IO; use Ada.Text_IO;
-- La representacion de los numeros de Church en ada no es directa, por lo q se hizo lo siguiente
procedure pregunta1b is 
  -- Creamos un tipo Church 
  type Church is record
      Valor: Integer;
      Next: access Church;
   end record;
   -- Apuntador
   type Apuntador_Church is access all Church;

  -- Procedimiento que para un numero cualquiera me devuelve su sucesor
  procedure Suc (N :in out Apuntador_Church) is
      -- Creamos el Sucesor numero que sera el sucesor del n
      Sucesor: Apuntador_Church := new Church'(Valor => N.Valor+1,Next => null);
   begin
      -- Actualizamos los valores
      Sucesor.Next:= N;
      N:= Sucesor;
   end Suc;

  -- Funcion que suma numerales de Church
  function Suma (A,B : Apuntador_Church) return Apuntador_Church is
      C:Apuntador_Church := new Church'(Valor =>A.Valor+B.Valor, Next => null);
   begin
      return C;
   end Suma;

  -- Funcion que multiplica numerales de Church
  function Multiplicacion (A,B : Apuntador_Church) return Apuntador_Church is
      C: Apuntador_Church := new Church'(Valor=> A.Valor*B.Valor,Next => null);
   begin
      return C;
   end Multiplicacion;
begin
  declare
      -- Mini ejemplo de como funciona church 
      Uno: Apuntador_Church := new Church'(Valor => 0, Next => null);
      Dos: Apuntador_Church := new Church'(Valor => 0, Next => null);
      Respuesta: Apuntador_Church;
   begin
      Suc(Uno);
      Suc(Dos);
      Suc(Dos);
      Respuesta := Suma(Uno,Dos);
      -- Imprimimos la suma
      Put_Line("1+2 es: " & Integer'Image(Respuesta.Valor));
      Respuesta := Multiplicacion(Uno,Dos);
      -- Imprimimos la multiplicacion
      Put_Line("1*2 es: " & Integer'Image(Respuesta.Valor));
   end;
end pregunta1b;

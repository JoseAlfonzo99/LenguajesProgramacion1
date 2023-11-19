-- Jose Alfonzo 17-10012 

---  pregunta 1)b)ii)
with Ada.Text_IO; use Ada.Text_IO;
-- La representacion de los numeros de Church en ada no es directa, por lo q se hizo lo siguiente
procedure pregunta1bii is 
  -- Parte ii) Arbol con información en ramas y hojas
  -- Creamos un tipo arbol binario 
  type Arbol is record
      -- Creamos su valor, y sus dos hijos,izquierdo y derecho
      Valor : Integer;
      Izq: access Arbol;
      Der : access Arbol;
   end record;

  -- Funcion que determina si es simetrico un arbol
  function esSimetrico(ARBOL1,ARBOL2: access Arbol) return Boolean is
   begin
      -- Si los arboles no tienen nada, es simetrico, ya que nada es igual a nada
      if ARBOL1 = null and ARBOL2 = null then
         return True;
      -- Si los arboles tienen algo, ese algo tiene que ser simetrico de ambos    
      elsif ARBOL1 /= null and ARBOL2 /= null then
         return (ARBOL1.Valor=ARBOL2.Valor) and esSimetrico(ARBOL1.Izq,ARBOL2.Der) and esSimetrico(ARBOL1.Der,ARBOL2.Izq);
      else
         return False;
      end if;
   end esSimetrico;

  -- Funcion que arroja un bool para saber si el arbol es un max heap simetrico 
  function boolMaxHeapSim (Tree : access Arbol) return Boolean is
   begin
      -- Comenzamos a ver si el tree tiene las propiedades de un max heap simetrico
      if Tree = null then
         return True;
      elsif Tree.Izq /= null and then Tree.Izq.Valor> Tree.Valor then
         return False;
      elsif Tree.Der /= null and then Tree.Der.Valor >Tree.Valor then
         return False;
      else
         return boolMaxHeapSim (Tree.Izq) and then boolMaxHeapSim (Tree.Der) and then esSimetrico(Tree.Izq,Tree.Der);
      end if;
   end boolMaxHeapSim;
begin
  declare
      -- Mini ejemplo de como funciona max heap simetrico
      Ejemplo : access Arbol := new Arbol'(Valor =>10,Izq => new Arbol'(Valor =>5, Izq => new Arbol'(Valor =>4,Izq => null,Der => null),Der => new Arbol'(Valor => 4, Izq => null, Der => null)),
       Der => new Arbol'(Valor=> 5, Izq => new Arbol'(Valor =>4,Izq => null, Der => null),Der => new Arbol'(Valor =>4, Izq => null,Der => null)));

       --        10
       --     /      \
       --   5         5
       --  / \       / \
       -- 4   4     4   4
   begin
      -- Imprimimos que el arbol si es un max heap simetrico
      Put_Line("Es un max heap simetrico el arbol ingresado? = " & Boolean'Image(boolMaxHeapSim(Ejemplo)));
   end;
end pregunta1bii;

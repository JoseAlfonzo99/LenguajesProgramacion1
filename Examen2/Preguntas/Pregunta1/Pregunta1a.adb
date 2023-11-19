-- Jose Alfonzo 17-10012 

---  pregunta 1)a)
with Ada.Text_IO;
with Ada.Integer_Text_IO;
with Ada.Text_IO; use Ada.Text_IO;


procedure Main is
   A : Integer := 10;
   B : Integer := 0;
begin
   if B = 0 then
      raise Program_Error;
   else
      Put_Line("A / B = " & Integer'Image(A/B));
   end if;
exception
   when Program_Error =>
      Put_Line("Error: Division by zero");
end Main;



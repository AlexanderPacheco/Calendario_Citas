Feature: Creacion de una receta

  Scenario: Se requiere crear una receta
     Given Existen citas creadas
      When Cuando se pulse el boton agregar receta
      Then Se crea una nueva receta para la cita
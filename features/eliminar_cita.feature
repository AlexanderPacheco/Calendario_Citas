Feature: Elimincion de citas

  Scenario: Se quiere eliminar una cita
     Given Existen citas registradas
      When Cuando se pulse el boton eliminar cita
      Then Se elimina la cita
    

    
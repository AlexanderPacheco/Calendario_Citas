Feature: Elimincion de pacientes

  Scenario: Se quiere eliminar un paciente
     Given Existen pacientes registrados 
      When Cuando se pulse el boton eliminar
      Then Se elimina el paciente
    
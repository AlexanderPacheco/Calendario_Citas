Feature: Creacion de una cita

  Scenario: Se requiere crear una cita
     Given Existen pacientes registrados 
      When Cuando se pulse el boton agendar cita
      Then Se crea una nueva cita para el paciente
    
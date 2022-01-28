Feature: Creacion de un examen clinico

  Scenario: Se requiere crear un examen clinico
     Given Existen citas creadass
      When Cuando se pulse el boton generar examen clinico
      Then Se crea un nuevo examen para la cita del paciente asociado
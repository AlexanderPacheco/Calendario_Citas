Feature: Modificar examen

  Scenario: Se requiere modificar un examen
    Given Existen examenes registrados
    When Cuando pulse el boton modificar examen
    Then Modifico mis campos y guardo el examen
    
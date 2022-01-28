Feature: Generacion de historial medico de los pacientes

  Scenario: Se requiere crear un reporte del historial medico de pacientes
     Given Se han atendido pacientes
      When Cuando se pulse el boton generar historial medico de pacientes
      Then Se visualiza el pdf generado del reporte general
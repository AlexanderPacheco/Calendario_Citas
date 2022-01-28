Feature: Generacion de historial medico de los pacientes

  Scenario: Se requiere crear un reporte de la concurrencia en la clinica
     Given Se han registrado citas
      When Cuando se pulse el boton generar reporte concurrencia
      Then Se visualiza el pdf generado del reporte de concurrencia
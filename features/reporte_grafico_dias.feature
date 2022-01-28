Feature: Generacion de reporte grafico de dias concurridos

  Scenario: Se requiere tener citas creadas
     Given Se han atendido citas
      When Cuando se pulse el boton generar reporte de dias concurridos
      Then Se visualiza reporte grafico
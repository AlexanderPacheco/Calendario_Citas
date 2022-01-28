Feature: Generacion de reporte grafico de meses concurridos

  Scenario: Se requiere tener citas creadass
     Given Se han atendido citass
      When Cuando se pulse el boton generar reporte de meses concurridos
      Then Se visualiza el reporte grafico
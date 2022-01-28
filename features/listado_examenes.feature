Feature: Listar Examenes

Scenario: Se requiere listar los examenes
    Given Se han mandado a realizar examenes 
    When Cuando se visite la pagina listado_examenes
    Then Se ven los examenes que se han realizado
    

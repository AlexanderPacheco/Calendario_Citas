Feature: Enviar notificacion email a paciente

Scenario: Se requiere enviar una notificacion de recordatorio de cita
    Given Existen citas creadas
    When Exista una cita para el dia siguiente
    Then Se envia un correo electronico al paciente


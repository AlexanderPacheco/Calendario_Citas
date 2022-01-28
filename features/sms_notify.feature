Feature: Enviar notificacion sms a paciente

Scenario: Se requiere enviar una notificacion sms de recordatorio de cita
    Given Existen citas creadas en el sistema
    When Exista una cita agendada para el dia siguiente
    Then Se envia un sms al paciente
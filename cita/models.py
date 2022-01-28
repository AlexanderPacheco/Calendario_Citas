from django.db import models
from django.urls import reverse
from users.models import Paciente
# Create your models here.
class Cita(models.Model):
    ESTADO_OPCIONES = [
        ('PENDIENTE', 'Pendiente'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
    ]
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_OPCIONES, default='PENDIENTE')
    comentario = models.CharField(max_length=50)
    # paciente = models.IntegerField()
    paciente = models.ForeignKey("users.Paciente", related_name="citas", on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse("cita_detail", kwargs={"pk": self.pk})
    

class Receta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    detalle_receta = models.CharField(max_length=300)
    cita = models.ForeignKey("Cita", related_name="recetas", on_delete=models.CASCADE, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, related_name="recetasPaciente", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.detalle_receta
    
    def get_absolute_url(self):
        return reverse("receta_detail", kwargs={"pk": self.pk})
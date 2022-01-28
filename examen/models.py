from django.db import models
from django.urls import reverse
from cita.models import Cita

class Examen(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=300)
    cita = models.ForeignKey(Cita, related_name="examenes", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.descripcion
    
    def get_absolute_url(self):
        return reverse("examination_detail", kwargs={"pk": self.pk})
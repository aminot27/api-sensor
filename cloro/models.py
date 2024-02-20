from django.db import models

# Create your models here.

class CloroModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    UNSAAC_TESIS_ELECTRONICA = models.CharField(max_length=255, verbose_name="Nombre del Sistema")
    data_cloro = models.CharField(max_length=10, verbose_name="Dato de Cloro")
    data_turbidez = models.CharField(max_length=10, verbose_name="Dato de Turbidez")

    class Meta:
        db_table = "cloro"
        ordering = ['-created_at']
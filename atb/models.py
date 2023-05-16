from django.conf import settings
from django.db import models
from django.utils import timezone
from pathlib import Path


class Reportaje(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField( default=timezone.now)
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    imagen = models.FileField(upload_to=BASE_DIR / 'imagenes', unique=True)
    

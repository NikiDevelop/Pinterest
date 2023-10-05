from django.db import models

class Pinterest(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="pinterest", null=True, blank=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo

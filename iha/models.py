from django.db import models


# Create your models here.

class Iha(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    marka = models.CharField(max_length=50,verbose_name="Marka")
    model =models.CharField(max_length=50,verbose_name="Model")
    weight = models.CharField(max_length=50,verbose_name="Ağırlık")
    category=models.CharField(max_length=50,verbose_name="Kategori")
    image = models.FileField(blank = True,null = True,verbose_name="Fotoğraf Ekleyin")
    def __str__(self):
        return self.marka
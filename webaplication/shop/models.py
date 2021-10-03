from django.db import models


class Producent(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=30)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(upload_to='', blank=True)
    descriptions = models.CharField(max_length=350, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"






from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import AbstractUser


class PhoneTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BasicPhone(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tag = models.ForeignKey(PhoneTag, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red"),
        ("#008000", "green"),
        ("#00FF00", "lime"),
        ("#0000FF", "blue"),
        ("#FFFF00", "yellow"),
        ("#575757", "grey"),
    ]
    color = ColorField(choices=COLOR_CHOICES)
    price = models.IntegerField()


    def __str__(self):
        return self.product_name


class ExtraPhone(models.Model):
    basic_product = models.ForeignKey(BasicPhone, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red"),
        ("#008000", "green"),
        ("#00FF00", "lime"),
        ("#0000FF", "blue"),
        ("#FFFF00", "yellow"),
        ("#575757", "grey"),
    ]
    color = ColorField(choices=COLOR_CHOICES)

class Laptop(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    processor = models.CharField(max_length=100)
    graphics = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    price = models.IntegerField()

# Create your models here.

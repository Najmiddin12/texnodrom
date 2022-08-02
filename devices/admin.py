from django.contrib import admin
from .models import *

@admin.register(PhoneTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(BasicPhone)
class BasicProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "brand", "model", "tag", "image", "color", "price")

@admin.register(ExtraPhone)
class ExtraProductAdmin(admin.ModelAdmin):
    list_display = ("basic_product", "image", "color")

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ("product_name", "image", "processor", "graphics", "memory", "price")
# Register your models here.

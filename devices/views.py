from django.shortcuts import render
from .models import PhoneTag, BasicPhone, ExtraPhone, Laptop
from next_prev import next_in_order, prev_in_order

def home(request):
    tag = PhoneTag.objects.all()
    basic_product = BasicPhone.objects.all()
    extra_product = ExtraPhone.objects.all()
    laptop = Laptop.objects.all()

    return render(request, "devices/home.html", {"basic_product": basic_product, "tag": tag, "extra_product": extra_product,
                                                 "laptop": laptop})




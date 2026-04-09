from django.shortcuts import render
from .models import Supplier, WaterBottle

# Create your views here.

def home(request):
    return render(request, 'MyInventoryApp/base.html')

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {"suppliers": suppliers})


def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {"bottles": bottles})

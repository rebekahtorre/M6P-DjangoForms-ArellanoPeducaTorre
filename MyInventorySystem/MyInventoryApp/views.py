from django.shortcuts import render
from .models import Supplier, WaterBottle, Account

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

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if Account.objects.filter(username=username, password=password):
            return render(request, "MyInventoryApp/view_supplier.html")
        else:
            return render(request, "MyInventoryApp/login.html", {"error": "Invalid login"})
    
    return render(request, "MyInventoryApp/login.html")

def signup(request):
    message = ""
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if Account.objects.filter(username=username):
            message = "Account already exists"

            return render(request, "MyInventoryApp/signup.html",{
                "message": message
        })

        else:
            Account.objects.create(username=username, password=password)
            message = "Account created successfully"
            
            return render(request, 'MyInventoryApp/login.html',{
                "message":message
            })
        
    return render(request, 'MyInventoryApp/signup.html')


    
    

from django.shortcuts import render, get_object_or_404, redirect
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

        account = Account.objects.filter(username=username, password=password)
    
        if len(account) > 0:
            return render(request, "MyInventoryApp/view_supplier.html")
        else:
            return render(request, "MyInventoryApp/login.html", {"error": "Invalid login"})
    
    return render(request, "MyInventoryApp/login.html")

def signup(request):
    message = ""
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        existing_accounts = Account.objects.filter(username=username)

        if len(existing_accounts > 0):
            message = "Account already exists"

            return render(request, "MyInventoryApp/signup.html",{
                "message": message
        })

        else:
            new_account = Account()
            new_account.username = username
            new_account.password = password
            new_account.save()
            message = "Account created successfully" 
            
            return render(request, 'MyInventoryApp/login.html',{
                "message":message
            })
        
    return render(request, 'MyInventoryApp/signup.html')

def view_bottle_details(request, pk):
    bottle = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/view_bottle_details.html', {"bottle": bottle})

def delete_bottle(request, pk):
    bottle = get_object_or_404(WaterBottle, pk=pk)
    bottle.delete()
    return redirect('view_bottles')
    
    

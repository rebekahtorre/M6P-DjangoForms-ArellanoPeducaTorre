from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier, WaterBottle, Account

<<<<<<< HEAD
# Create your views here.
=======
current_pk = None
msg = None
>>>>>>> 17a9645efca2c4f3132ced980d3ce2257809ae55

def home(request):
    return render(request, 'MyInventoryApp/base.html', {"pk": current_pk})

def add_bottle(request):
<<<<<<< HEAD
    return render(request, 'MyInventoryApp/add_bottle.html')

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {"suppliers": suppliers})

=======
    suppliers = Supplier.objects.all()

    if request.method == "POST":
        sku = request.POST.get("sku")
        brand = request.POST.get("brand")
        cost = request.POST.get("cost")
        size = request.POST.get("size")
        mouth_size = request.POST.get("mouth_size")
        color = request.POST.get("color")
        supplied_by = request.POST.get("supplied_by")
        current_quantity = request.POST.get("current_quantity")
        if WaterBottle.objects.filter(sku=sku):
            return render(request, 'MyInventoryApp/add_bottle.html', {"message": "SKU already exists", "suppliers": suppliers})
        
        supplier = Supplier.objects.get(pk=supplied_by)
        WaterBottle.objects.create(sku=sku, brand=brand, cost=cost, size=size, mouth_size=mouth_size, color=color, supplied_by=supplier, current_quantity=current_quantity)
    
    return render(request, 'MyInventoryApp/add_bottle.html', {"suppliers": suppliers})

def view_supplier(request):
    global msg
    msg = None
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {"suppliers": suppliers, "pk": current_pk})
>>>>>>> 17a9645efca2c4f3132ced980d3ce2257809ae55

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {"bottles": bottles, "pk": current_pk})

def view_bottle_details(request, pk):
    bottle = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/view_bottle_details.html', {"bottle": bottle, "bottle.pk": bottle.pk})

def delete_bottle(request, pk):
    if request.method == "POST":
        bottle = get_object_or_404(WaterBottle, pk=pk)
        bottle.delete()
    return redirect('view_bottles')

def login(request):
    global msg
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        account = Account.objects.filter(username=username, password=password)
<<<<<<< HEAD
    
        if len(account) > 0:
            return render(request, "MyInventoryApp/view_supplier.html")
        else:
            return render(request, "MyInventoryApp/login.html", {"error": "Invalid login"})
    
=======
        if account:
            acc = account[0]
            global current_pk
            current_pk = acc.pk
            return redirect('view_supplier')
        else:
            return render(request, "MyInventoryApp/login.html", {"error": "Invalid login"})
    if msg:
        return render(request, "MyInventoryApp/login.html", {"message": msg})
>>>>>>> 17a9645efca2c4f3132ced980d3ce2257809ae55
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
<<<<<<< HEAD
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
    
    
=======
            Account.objects.create(username=username, password=password)
            global msg
            msg = "Account created successfully"
            return redirect('login')

    return render(request, 'MyInventoryApp/signup.html')

def manage_account(request, pk):
    acc = get_object_or_404(Account, pk=current_pk)
    return render(request, "MyInventoryApp/manage.html", {"acc": acc, "pk": current_pk})

def change_password(request, pk):
    acc = get_object_or_404(Account, pk=current_pk)

    if request.method == "POST":
        current = request.POST.get("current_password")
        new1 = request.POST.get("new_password1")
        new2 = request.POST.get("new_password2")

        if current == acc.password and new1 == new2:
            Account.objects.filter(pk=current_pk).update(password=new1)
            return redirect('manage_account', pk=current_pk)
        else:
            return render(request, "MyInventoryApp/change_password.html", {"acc": acc, "message": "Invalid password change", "pk": current_pk})

    return render(request, "MyInventoryApp/change_password.html", {"acc": acc, "pk": current_pk})

def delete_account(request, pk):
    global current_pk
    Account.objects.filter(pk=current_pk).delete()
    current_pk = None
    return redirect('login')

def logout(request):
    global current_pk
    current_pk = None
    return redirect('login')
>>>>>>> 17a9645efca2c4f3132ced980d3ce2257809ae55

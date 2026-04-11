from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, WaterBottle, Account

current_pk = None

def home(request):
    return render(request, 'MyInventoryApp/base.html', {"pk": current_pk})

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html', {"pk": current_pk})

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {"suppliers": suppliers, "pk": current_pk})

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {"bottles": bottles, "pk": current_pk})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        acc_qs = Account.objects.filter(username=username, password=password)
        if acc_qs:
            acc = acc_qs[0]
            global current_pk
            current_pk = acc.pk
            return redirect('view_supplier')
        else:
            return render(request, "MyInventoryApp/login.html", {"error": "Invalid login"})

    return render(request, "MyInventoryApp/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if Account.objects.filter(username=username):
            return render(request, "MyInventoryApp/signup.html", {"message": "Account already exists"})
        else:
            Account.objects.create(username=username, password=password)
            return render(request, 'MyInventoryApp/login.html', {"message": "Account created successfully"})

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
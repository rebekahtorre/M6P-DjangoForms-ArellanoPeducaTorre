from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, WaterBottle, Account

def home(request):
    return render(request, 'MyInventoryApp/base.html')

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')

def view_supplier(request, pk):
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/view_supplier.html', {"suppliers": suppliers, "pk": pk})

def view_bottles(request):
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {"bottles": bottles})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        acc_qs = Account.objects.filter(username=username, password=password)
        if acc_qs:
            acc = acc_qs[0]
            return redirect('view_supplier', pk=acc.pk)
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
    acc = get_object_or_404(Account, pk=pk)
    return render(request, "MyInventoryApp/manage.html", {"acc": acc})

def change_password(request, pk):
    acc = get_object_or_404(Account, pk=pk)

    if request.method == "POST":
        current = request.POST.get("current_password")
        new1 = request.POST.get("new_password1")
        new2 = request.POST.get("new_password2")

        if current == acc.password and new1 == new2:
            Account.objects.filter(pk=pk).update(password=new1)
            return redirect('manage_account', pk=pk)
        else:
            return render(request, "MyInventoryApp/change_password.html", {"acc": acc, "message": "Invalid password change"})

    return render(request, "MyInventoryApp/change_password.html", {"acc": acc})

def delete_account(request, pk):
    Account.objects.filter(pk=pk).delete()
    return redirect('login')

def logout(request):
    return redirect('login')
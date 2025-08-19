from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomerModel
from django.db.models import Q

# Create your views here.

@login_required(login_url='login/')
def home_view(request):
    customer_details = CustomerModel.objects.all()
    
    if request.method == 'GET':
        search_data = request.GET.get('search', '').strip()
        
        if search_data:
            customer_details = CustomerModel.objects.filter(
                Q(fullname__icontains=search_data) |
                Q(email__icontains=search_data)
            )

    
    return render(request, 'home/home.html', {'context':customer_details})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        login(request, user)
        print(user)
        
        return redirect('home_view')
    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    
    return redirect('login_view')

def register_view(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        
        CustomerModel.objects.create(
            fullname=fullname,
            email=email,
            mobile=mobile,
            address=address
        )
        
        return redirect('home_view')
        
    return render(request, 'register/register.html')

def update_cust_data_view(request, id):
    cust_data = CustomerModel.objects.get(id=id)
    
    if request.method == 'POST':
        fullname = request.POST['fullname']
        address = request.POST['address']
        
        cust_data.fullname=fullname
        cust_data.address=address
        
        cust_data.save()
        
        return redirect('home_view')
    
    return render(request, 'update_cust_data/update.html', {'context':cust_data})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AdminRegisterForm, CustomerRegisterForm
from .models import Admin, Customer,Product
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import LoginForm,ProductForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        if 'admin_submit' in request.POST:  # Admin Registration
            form = AdminRegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                

                # Check if admin already exists
                if User.objects.filter(username=email).exists():
                    messages.error(request, "Admin with this email already exists.")
                else:
                    # Create Django User and Admin Entry
                    user = User.objects.create_superuser(username=email, email=email, password=password)
                    Admin.objects.create(email=email, password=password)  # ✅ Store password
                    
                    return redirect('home')

        elif 'customer_submit' in request.POST:  # Customer Registration
            form = CustomerRegisterForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                address = form.cleaned_data['address']
                mobile_no = form.cleaned_data['mobile_no']

                

                # Check if customer already exists
                if User.objects.filter(username=email).exists():
                    messages.error(request, "Customer with this email already exists.")
                else:
                    # Create Django User and Customer Entry
                    user = User.objects.create_user(username=email, email=email, password=password)
                    Customer.objects.create(c_name=name, c_email=email, password=password, address=address, mobile_no=mobile_no)  # ✅ Store password
                    
                    return redirect('home')

    else:
        admin_form = AdminRegisterForm()
        customer_form = CustomerRegisterForm()

    return render(request, 'register.html', {'admin_form': admin_form, 'customer_form': customer_form})

def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                admin = Admin.objects.get(email=email)
                

                if admin.password == password:
            
                    print("✅ Redirecting to Admin Dashboard")
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
                else:
                    print("❌ Incorrect Password")
                    messages.error(request, "Invalid email or password.")
            except Admin.DoesNotExist:
                print("❌ Admin Does Not Exist")
                messages.error(request, "Invalid email or password.")
    
    else:
        form = LoginForm()
    
    return render(request, 'admin_login.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                customer = Customer.objects.get(c_email=email)
                if customer.password == password:  # ✅ Manual password check
                    
                    return redirect('customer_dashboard')  # Redirect to customer product list
                else:
                    messages.error(request, "Invalid email or password.")
            except Customer.DoesNotExist:
                messages.error(request, "Invalid email or password.")
    
    else:
        form = LoginForm()
    
    return render(request, 'customer_login.html', {'form': form})

def admin_dashboard(request):
    products = Product.objects.all()
    return render(request, 'admin_dashboard.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('admin_dashboard')

def customer_dashboard(request):
    products = Product.objects.all()
    return render(request, 'customer_dashboard.html', {'products': products})


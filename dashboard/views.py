from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Product,Order
from.forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required(login_url='user_login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    workers = User.objects.all()
    product_count = products.count()
    orders_count = orders.count()
    workers_count = workers.count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user #the staff that is making the request
            instance.save()
            return redirect('dashboard_index')
    else:
        form = OrderForm()

    context = {
        'orders':orders,
        'form':form,
        'products':products,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count,

    }
    return render(request, 'dashboard/index.html', context)




@login_required(login_url='user_login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    items_count = Product.objects.all().count()

    context = {
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'items_count':items_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url='user_login')
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)

    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url='user_login')
def product(request):

    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    items = Product.objects.all() #using ORM
    items_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            redirect('product')
    else:
        form = ProductForm()

    context = {
        'items':items,
        'form': form,
        'workers_count':workers_count,
        'items_count':items_count,
        'orders_count':orders_count,
         
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user_login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    items_count = Product.objects.all().count()
   
    context = {
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'items_count':items_count,
    }
    return render(request, 'dashboard/order.html', context)

@login_required(login_url='user_login')
def product_delete(request, pk):
    item = Product.objects.get(id = pk)
    if request.method == "POST":
        item.delete()
        return redirect('product')
    return render(request, 'dashboard/product_delete.html')

@login_required(login_url='user_login')
def product_update(request, pk):
    item = Product.objects.get(id = pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')

    else:
        form = ProductForm(instance=item)
    context = {
            'form':form
    }

    return render(request, 'dashboard/product_update.html', context)
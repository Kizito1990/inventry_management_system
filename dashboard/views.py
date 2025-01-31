from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Product
from.forms import ProductForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='user_login')
def index(request):
    return render(request, 'dashboard/index.html')




@login_required(login_url='user_login')
def staff(request):
    workers = User.objects.all()

    context = {
        'workers':workers
    }
    return render(request, 'dashboard/staff.html', context)


def staff_detail(request):
    return render(request, 'dashboard/staff_detail.html')

@login_required(login_url='user_login')
def product(request):

    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    items = Product.objects.all() #using ORM

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('product')
    else:
        form = ProductForm()

    context = {
        'items':items,
        'form': form
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user_login')
def order(request):
    return render(request, 'dashboard/order.html')


def product_delete(request, pk):
    item = Product.objects.get(id = pk)
    if request.method == "POST":
        item.delete()
        return redirect('product')
    return render(request, 'dashboard/product_delete.html')

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
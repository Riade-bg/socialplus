from django.http      import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from .forms import RawFormClass

def show(request, id):
    obj = Product.objects.get(id=id)
    context = {
        "obj" : obj
    }
    return render(request, "product/product_create.html", context)

# def create_product(request, id):
#     initial = {
#         'title': 'This is title'
#     }
#     form = ProductForm(request.POST or None, initial=initial)
#     if form.is_valid():
#         form.save()
#     context = {
#         "form": form
#     }
#     return render(request, "product/product_create.html", context)
    
# def delete(request, id):
#     obj = get_object_or_404(Product, id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect('../')
#     context = {
#         "obj" : obj
#     }
#     return render(request, "product/delete.html", context)

def product(request):
    obj = Product.objects.all()
    # obj = ProductForm(Product, id=id)
    context = {
        "object_list": obj,
    }
    return render(request, "product/details.html", context)
    
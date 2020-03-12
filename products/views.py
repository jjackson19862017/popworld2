from django.shortcuts import render, redirect, reverse
from .models import Product
from .forms import ProductsForm
from django.contrib import messages

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products":products})

def addproducts(request):
    print("Loaded view")
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("Posted???")
        # create a form instance and populate it with data from the request:
        APF = ProductsForm(request.POST, request.FILES)
        print("Yes it has been")
        # check whether it's valid:
        if APF.is_valid():
            APF.save()
            messages.error(request, "Product Added!")
            print("Hey the Forms Valid")

            return render(request, "addproducts.html", {'APF': APF})
        else:
                messages.error(request, "Unable to ADD this product.")
                print("Not Valid")
    # if a GET (or any other method) we'll create a blank form
    else:
        APF = ProductsForm()

    return render(request, "addproducts.html", {'APF': APF})

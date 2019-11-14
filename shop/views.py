from django.shortcuts import render
from .models import Product
from math import  ceil
from django.http import HttpResponse


def product(request):

    allProds = []
    catProds = Product.objects.values('p_category', 'p_id')
    cats = {item['p_category'] for item in catProds}

    for cat in cats:
        prod = Product.objects.filter(p_category = cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - n // 4)
        allProds.append([prod, range(1,nslides), nslides])

    params = {'allProds': allProds}
    return render(request,'work.html',params)

def product_details(request, id):
    print(id)
    product = Product.objects.filter(p_id = id)
    context = {'product':product}
    return render(request, 'product_details.html',context)

def details(request):
    return HttpResponse("details")

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


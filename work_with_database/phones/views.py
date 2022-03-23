from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': Phone.objects.order_by(sort(request.GET.get('sort')))}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone':phone}
    print(context)
    return render(request, template, context)


def sort(value):
    values_dict = {'name': 'name', 'max_price': '-price', 'min_price': 'price'}
    if value in values_dict.keys():
        return values_dict[value]
    else:
        return 'id'

from django.http import HttpResponse
from django.shortcuts import render
from app.models import Product


def show(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'show.html', context)


def signup(request):
    name = request.GET.get("name")
    price = request.GET.get("price")
    # insert
    p = Product(name=name, price=price)
    p.save()
    return HttpResponse('상품 등록 완료')


def index(request):
    return HttpResponse("hello")


def html(request):
    context = {}  # dictionary
    return render(request, 'html.html', context)  # 3 parameters

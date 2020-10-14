from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from datetime import datetime


# Create your views here.

def index(request):
    products = Product.objects.all()  # taking out all products
    print(products)

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides) ,'product':products}  #arguments for templatel only for single slider
    # allproducts = [[products, range(1, nSlides), nSlides],[products, range(1, nSlides), nSlides]]
    allproducts = []
    cat_products = Product.objects.values('category', 'id')
    category = {item['category'] for item in cat_products}
    for cat in category:
        prod = Product.objects.filter(category=cat)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))  # this formula calculates the number of slides needed
        allproducts.append([prod, range(1, nSlides), nSlides])
    params = {'allproducts': allproducts}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        submitbtn = True
        return render(request, "shop/contact.html", {'submitbtn': submitbtn})
    return render(request, "shop/contact.html")

def searchMate(query, item):
    '''return true only if query matches the item'''
    if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allproducts = []
    cat_products = Product.objects.values('category', 'id')
    category = {item['category'] for item in cat_products}
    for cat in category:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMate(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))  # this formula calculates the number of slides needed
        if len(prod) != 0:
            allproducts.append([prod, range(1, nSlides), nSlides])
    params = {'allproducts': allproducts, "msg": ""}
    if len(allproducts) == 0 or len(query)<2 :
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, "shop/search.html", params)


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/productView.html", {'product': product[0]})


def track(request):
        # formateDate = myDate.strftime("%d-%B-%Y, %H:%M:%S")
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if (len(order)) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success","updates": updates, "itemJson": order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"no item"}')

        except Exception:
            return HttpResponse('{"status": "error"}')

    return render(request, "shop/track.html")


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')

        order = Orders(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city,
                       state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your Order has been Placed")
        update.save()

        thank = True
        id = order.order_id
        return render(request, "shop/checkout.html", {'thank': thank, 'id': id})
    return render(request, "shop/checkout.html")

from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product, Contact, Order
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catProds = Product.objects.values('category','id') #<QuerySet [{'category': 'Electronics', 'id': 7}, {'category': 'Electronics', 'id': 8}, {'category': 'Footwear', 'id': 9}, {'category': 'Cloths', 'id': 10}, {'category': 'Electronics', 'id': 11}, {'category': 'Electronics', 'id': 12}, {'category': 'Electronics', 'id': 13}, {'category': 'Electronics', 'id': 14}]>
    categories_set = { item['category'] for item in catProds} #here we use set instead of list because we dont need repetation of Catergories
    for category in categories_set:
        products_of_this_category = Product.objects.filter(category=category) # gives products of a spcific category
        n = len(products_of_this_category) #no of prods of this category to make slides
        nSlides = ceil(n/4)
        allProds.append([products_of_this_category, range(1, nSlides), nSlides]) # alag alag category ka ek ek list tyaar ho jayega aur all prods mein append ho jayega (allProds is List of List)
    params = {"allProds": allProds}
    print("All Prods= ",allProds)
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method =='POST':
        name = request.POST.get('name'," ")
        email = request.POST.get('email'," ")
        field = request.POST.get('field'," ")
        prime = request.POST.get('prime'," ")
        message = request.POST.get('message'," ")
        contact = Contact(name=name, email=email, field=field, prime_status=prime, desc=message)
        contact.save()
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
     return render(request, "shop/search.html")


def productView(request, myid):
    #Fetching the product by it's Id
    product = Product.objects.filter(id=myid) # this gives you the list og 1 product
    params = {'product': product[0]}
    return render(request, "shop/product.html", params ) #sending the product


def checkout(request):
    allProds = []
    catProds = Product.objects.values('category','id') #<QuerySet [{'category': 'Electronics', 'id': 7}, {'category': 'Electronics', 'id': 8}, {'category': 'Footwear', 'id': 9}, {'category': 'Cloths', 'id': 10}, {'category': 'Electronics', 'id': 11}, {'category': 'Electronics', 'id': 12}, {'category': 'Electronics', 'id': 13}, {'category': 'Electronics', 'id': 14}]>
    categories_set = { item['category'] for item in catProds} #here we use set instead of list because we dont need repetation of Catergories
    for category in categories_set:
        products_of_this_category = Product.objects.filter(category=category) # gives products of a spcific category
        n = len(products_of_this_category) #no of prods of this category to make slides
        nSlides = ceil(n/4)
        allProds.append([products_of_this_category, range(1, nSlides), nSlides]) # alag alag category ka ek ek list tyaar ho jayega aur all prods mein append ho jayega (allProds is List of List)
    params = {"allProds": allProds}
    print("All Prods in Checkout= ",allProds)
    return render(request, "shop/checkout.html", params)

def order(request):
    if request.method =='POST':
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name'," ")
        email = request.POST.get('email'," ")
        phone = request.POST.get('phone'," ")
        address = request.POST.get('address'," ")
        city = request.POST.get('city'," ")
        state = request.POST.get('state'," ")
        zip_code = request.POST.get('zip_code'," ")
        order = Order(items_json=items_json,name=name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/order.html', {'thank':thank, 'id': id})

    allProds = []
    catProds = Product.objects.values('category','id') #<QuerySet [{'category': 'Electronics', 'id': 7}, {'category': 'Electronics', 'id': 8}, {'category': 'Footwear', 'id': 9}, {'category': 'Cloths', 'id': 10}, {'category': 'Electronics', 'id': 11}, {'category': 'Electronics', 'id': 12}, {'category': 'Electronics', 'id': 13}, {'category': 'Electronics', 'id': 14}]>
    categories_set = { item['category'] for item in catProds} #here we use set instead of list because we dont need repetation of Catergories
    for category in categories_set:
        products_of_this_category = Product.objects.filter(category=category) # gives products of a spcific category
        n = len(products_of_this_category) #no of prods of this category to make slides
        nSlides = ceil(n/4)
        allProds.append([products_of_this_category, range(1, nSlides), nSlides]) # alag alag category ka ek ek list tyaar ho jayega aur all prods mein append ho jayega (allProds is List of List)
    params = {"allProds": allProds}
    print("All Prods in Checkout= ",allProds)
    return render(request, "shop/order.html", params)
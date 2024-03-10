from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "visible"
    else:
        items =[]
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "visible"
        user_login = "hidden"
    id = request.GET.get('id', '')
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub = False)
    context= {'products':products,'categories':categories,'items':items, 'order':order, 'cartItems': cartItems, 'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'app/detail.html', context)
def category(request):
    categories = Category.objects.filter(is_sub = False)
    active_category = request.GET.get('category', '')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "visible"
    else:
        user_not_login = "visible"
        user_login = "hidden"
    context = {'categories':categories, 'products':products, 'active_category':active_category, 'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'app/category.html', context)
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "visible"
    else:
        items =[]
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "visible"
        user_login = "hidden"
    products = Product.objects.all()
    return render(request, 'app/search.html', {"search":search, "keys":keys, 'products': products, 'cartItems': cartItems, 'user_not_login':user_not_login, 'user_login':user_login})
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'app/register.html', context)
def loginPage(request):
    if request.user.is_authenticated: # is_authenticated : Xac thuc hay chua
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: messages.info(request, 'user or password not correct!')
            
    context = {}
    return render(request, 'app/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "visible"
    else:
        items =[]
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "visible"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    
    products = Product.objects.all()
    context= {'categories':categories,'products': products, 'cartItems': cartItems, 'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'app/home.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "visible"
    else:
        items =[]
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "visible"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    context= {'categories':categories,'items':items, 'order':order, 'cartItems': cartItems, 'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'app/cart.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        username = customer.username
        email = ''
        if (customer.email == None):
            email = ''
        else:
            email = customer.email
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        total = order.get_cart_total
        user_not_login = "hidden"
        user_login = "visible"
        
        # if request.method == 'POST':
        #     # username = request.POST.get('username')
        #     # email = request.POST.get('email')
        #     address = request.POST.get('address')
        #     city = request.POST.get('city')
        #     state = request.POST.get('state')
        #     phone = request.POST.get('phone')
            
        #     shipping = ShippingAddress(
        #         customer = customer,
        #         order = order,
        #         address = address,
        #         city = city,
        #         state = state,
        #         mobile = phone,
        #     )
        #     return JsonResponse({'status': 'success'})
        # else:
        #     return JsonResponse({'status': 'error'})
    else:
        items =[]
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "visible"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub = False)
    context= {'username':username, 'email':email, 'total':total,'categories':categories,'items':items, 'order':order, 'cartItems': cartItems, 'user_not_login':user_not_login, 'user_login':user_login}
    return render(request, 'app/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('added', safe=False)

def update_checkout(request):
    data = json.loads(request.body)
    _customer = request.user
    _order, created = Order.objects.get_or_create(customer = _customer, complete = False)
    _address = data['address']
    _city = data['city']
    _state = data['state']
    _phone = data['phone']
    shipping, created = ShippingAddress.objects.get_or_create(customer = _customer,
                                            order = _order,
                                            address = _address,
                                            city = _city,
                                            state = _state,
                                            mobile = _phone)
    shipping.save()
    _order.complete = True
    _order.save()
    
    # Lấy danh sách sản phẩm từ đơn hàng của user
    items = _order.orderitem_set.all()
    
    # Lấy địa chỉ email!
    email = _customer.email if _customer.email else settings.DEFAULT_FROM_EMAIL
    
    # Subject của email
    email_subject = 'ĐƠN HÀNG TỪ SHOP BONAA'
    # Nội dung email
    email_message = f'Kính gửi khách hàng:\t{_customer.username}\n'
    email_message += 'Shop BONAA xin gửi cho quý khách hàng thông tin đơn hàng:\n'
    email_message += f'Ngày giao dịch: {_order.date_order}\n'
    email_message += 'Danh sách sản phẩm:\n'
    for item in items:
        email_message += f'\t{item.product.name} - SL: {item.quantity} - Đơn giá: ${round(item.product.price, 2)}\n'
    email_message += f'Tổng xìn đơn hàng: ${round(_order.get_cart_total, 2)}\n'
    email_message += 'Cảm ơn quý khách đã ủng hộ sản phẩm của shop. Shop sẽ cố gắng ngày một hoàn thiện và cho ra mắt các sản phẩm chất lượng hơn trong tương lai nhằm mang lại trải nghiệm tốt nhất cho quý khách.'
    
    # Gửi email!
    send_mail(
        email_subject,
        email_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email,],
        fail_silently=False,
    )
    
    # _address = request.POST.get('address')
    # if (_address == None):
    #     return redirect('home')
    # else:
    #     return JsonResponse('added', safe=False)
    return JsonResponse('added', safe=False)
    
    
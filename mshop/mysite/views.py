#_*_ coding: utf-8 _*_
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from mysite import models, forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
import datetime
from cart.cart import Cart
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

def index(request, cat_id=0):
    all_categories = models.Category.objects.all()
    all_products = None
    if cat_id > 0:
        try:
            category = models.Category.objects.get(id=cat_id)
        except:
            category = None

        if category is not None:
            all_products = models.Product.objects.filter(category=category)
    if category is None:
        cate = 0
    else:
        cate = category.id

    if all_products is None:
        all_products = models.Product.objects.all()

    paginator = Paginator(all_products, 4)
    p = request.GET.get('p')
    try:
        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    cart = Cart(request)
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@login_required
def cart(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request)
    template = get_template('cart.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)    

def product(request, product_id):

    try:
        product = models.Product.objects.get(id=product_id)
    except:
        product = None

    template = get_template('product.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

def add_to_cart(request, cat_id, product_id, quantity):
    product = models.Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price, quantity)

    return redirect('/'+cat_id)

def remove_from_cart(request, product_id):
    product = models.Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('/cart/')

@verified_email_required
def order(request):
    all_categories = models.Category.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        new_order = models.Order(user=user) 

        form = forms.OrderForm(request.POST, instance=new_order)
        if form.is_valid():
            order = form.save()
            email_messages = "您的購物內容如下：\n"
            for item in cart:
                models.OrderItem.objects.create(order=order, 
                                          product=item.product,
                                          price = item.product.price,
                                          quantity=item.quantity)
                email_messages = email_messages + "\n" + \
                                "{}, {}, {}".format(item.product, item.product.price, item.quantity)
            email_messages = email_messages + \
                    "\n以上共計{}元\nhttp://mshop.min-haung.com感謝您的訂購！".format(cart.summary())
            messages.add_message(request, messages.INFO, "訂單已儲存，我們會儘快處理。")
            send_mail("感謝您的訂購", 
                       email_messages, 
                       '迷你小電商<ho@min-huang.com>',
                       [request.user.email],)
            send_mail("有人訂購產品囉", 
                       email_messages, 
                       '迷你小電商<ho@min-huang.com>',
                       ['skynet.tw@gmail.com'],)    
            cart.clear()       
            return redirect('/myorders/')
    else:
        form = forms.OrderForm()

    template = get_template('order.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@login_required
def payment(request, order_id):
    all_categories = models.Category.objects.all()
    try:
        order = models.Order.objects.get(id=order_id)
    except:
        messages.add_message(request, messages.WARNING, "訂單編號錯誤，無法處理付款。")
        return redirect('/myorders/')
    all_order_items = models.OrderItem.objects.filter(order=order)
    items = list()
    total = 0
    for order_item in all_order_items:
        t = dict()
        t['name'] = order_item.product.name
        t['price'] = order_item.product.price
        t['quantity'] = order_item.quantity
        t['subtotal'] = order_item.product.price * order_item.quantity
        total = total + order_item.product.price
        items.append(t)

    host = request.get_host()
    paypal_dict = {
        "business": settings.PAYPAL_REVEIVER_EMAIL,
        "amount": total,
        "item_name": "迷你小電商貨品編號:{}".format(order_id),
        "invoice": "invoice-{}".format(order_id),
        "currency_code": 'TWD',
        "notify_url": "http://{}{}".format(host, reverse('paypal-ipn')),
        "return_url": "http://{}/done/".format(host),
        "cancel_return": "http://{}/canceled/".format(host),
        }
    paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    template = get_template('payment.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@login_required
def my_orders(request):
    all_categories = models.Category.objects.all()
    orders = models.Order.objects.filter(user=request.user)

    template = get_template('myorders.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@csrf_exempt
def payment_done(request):
    template = get_template('payment_done.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

@csrf_exempt
def payment_canceled(request):
    template = get_template('payment_canceled.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

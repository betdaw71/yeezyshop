from django.shortcuts import render
from main.models import Product,Category,Cart,ProductToCart,ProductImage
from django.http import HttpResponse
#from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
import random 
#import re

# Create your views here.
def index(request):
	yeezy350 = Product.objects.filter(category = Category.objects.get(title='YEEZY BOOST 350'))
	yeezy500 = Product.objects.filter(category = Category.objects.get(title='YEEZY BOOST 500'))
	yeezy700 = Product.objects.filter(category = Category.objects.get(title='YEEZY BOOST 700'))
	yeezySlide = Product.objects.filter(category = Category.objects.get(title='YEEZY BOOST SLIDE'))

	try:
		cart = Cart.objects.get(user=request.session.session_key)
	except:
		request.session.create()
		cart = Cart.objects.create(user=request.session.session_key)
#	sale_p = Product.objects.filter(to_sale=True)
#	# sale_pa = all_p - sale_p	
	context = {
		'yeezy350':yeezy350,
        'yeezy500':yeezy500,
        'yeezy700':yeezy700,
        'slidee':yeezySlide,
        'cart':cart.productto.all(),
	}
	print(yeezySlide)
	return render(request,"main/index.html",context)

def add_to_cart(request,pk,size):
	try:
		cart = Cart.objects.get(user=request.session.session_key)
	except:
		request.session.create()
		cart = Cart.objects.create(user=request.session.session_key)
	pr = Product.objects.get(pk=pk)
#    pr.images.first.url
	ProductToCart.objects.create(title=pr.title,price=pr.price,size=size,image=ProductImage.objects.filter(product=pr).first().image.url,cart=cart)
	return HttpResponse('Product has been added')

def category(request,slug):
    category = Category.objects.get(slug=slug)
    yeezy = Product.objects.filter(category = category)
    
    context = {
        'category':category,
        'yeezy':yeezy
	}
    return render(request,"category/category.html",context)
def item(request,slug,pk):
    item = Product.objects.get(pk=pk)
    try:
        same = random_items = random.sample(list(Product.objects.filter(category = Category.objects.get(slug = slug))), 3)
    except:
        same = None
    may = random_items = random.sample(list(Product.objects.all()), 3)
    context={
        'item': item,
        'same' : same,
        'may' : may
    }
    return render(request,"item/item.html",context)

def get_cart(request):
	try:
		cart = Cart.objects.get(user=request.session.session_key)
	except:
		request.session.create()
		cart = Cart.objects.create(user=request.session.session_key)
	string = ''
	items = cart.productto.all()
	for i in items:
		string += '<div class="basket__item"id="%s"><img src="%s"><div class="wrapper"><div class="basket__item-desc">%s - %s</div><div class="basket__item-price"><span class="price__num"id="">%s</span><span><i class="fa fa-rub" aria-hidden="true"></i></span></div></div><div class="item__delete" id="%s"><i class="fa fa-trash delete" aria-hidden="true"></i></div></div>' % (i.pk,i.image,i.size,i.title,i.price,i.pk)
	return HttpResponse(string)


def add_cart(request):
	request.session.create() 
	Cart.objects.create(user=request.session.session_key)
	return HttpResponse('Cart has been created')


def delfromcart(request,pk):
    cart = Cart.objects.get(user=request.session.session_key)
    cart.productto.get(pk=pk).delete()
    return HttpResponse('Deleted from cart')

def getprice(request):
    cart = Cart.objects.get(user=request.session.session_key)
    items = cart.productto.all()
    summ = 0
    for i in items:
        summ += i.price
    
    return HttpResponse(str(summ))


def getsum(request):
    cart = Cart.objects.get(user=request.session.session_key)
    items = cart.productto.all()
    return HttpResponse(str(len(items)))

def order(request):
	if request.method == 'POST':
		name = request.POST['name'];
		mail = request.POST['mail'];
		number = request.POST['tel'];
		messageP = request.POST['message'];
		pay = request.POST['pay'];
		addres = request.POST['addres'];
		s = ''
		cart = Cart.objects.get(user=request.session.session_key)
		items = cart.productto.all()
		for i in items:
			s += '%s - %s' % (i.title , i.size)
			s += '\n'
		massage = 'Имя : ' + name + '\n Номер : ' + number + '\n E-mail : ' + mail + '\n Сообщение : ' + messageP + '\n Способ оплаты : ' + pay +' \nАдрес : ' + addres + ' \nЗаказ : \n' + s 
#		send_mail('Заявка на сайте minoxidilrussia.ru',massage,settings.EMAIL_HOST_USER,['minox.russia@mail.ru'])
		send_mail('Заявка на сайте weezyboost.ru',massage,settings.EMAIL_HOST_USER,['y3ezy.boost@yandex.ru'])
		return HttpResponse('')

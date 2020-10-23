from django.db import models
from django.contrib.sessions.models import Session
from django.utils.text import slugify


# Create your models here.

class Cart(models.Model):
    user = models.CharField(max_length=300)


class Category(models.Model):
    title = models.CharField(max_length=100,default='No Category')
    slug = models.SlugField(default='yeezysome')
    description = models.TextField(default='Some Description')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

    
class ProductToCart(models.Model):
    title = models.CharField(max_length=50)
#    description = models.CharField(max_length=1024)
    price = models.IntegerField()
#    to_sale = models.BooleanField(default=False) 
#    sale = models.IntegerField(blank=True)
#    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    size = models.TextField()
    image = models.TextField()
#    ratings = ArrayField(IntegerField())
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,related_name='productto')
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    price = models.IntegerField()
    to_sale = models.BooleanField(default=False) 
    sale = models.IntegerField(blank=True)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    size = models.TextField(default='37,5|38,5|39|39,5|40|41|41,5|42|43|43,5|44|44,5|45|46|46,5|47')
#    ratings = ArrayField(IntegerField())
#    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True)

    def get_sale(self):
        '''Расчитать стоимость со скидкой'''
        price = int(self.price * (100 - self.sale) / 100)
        return price
    def get_size(self):
        return self.size.split('|')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

#class Order(models.Model):
#    name = models.CharField(max_length=250)
#    mail = models.CharField(max_length=250)
#    phone = models.CharField(max_length=250)
#    massage = models.CharField(max_length=250,blank=True)
#    PAY_CHOICES = (
#        ('Cash', 'Наличные'),
#        ('Credit', 'Банковский перевод'),
#    )
#    paymant = models.CharField(max_length=250,choices=PAY_CHOICES)
#    addres = models.CharField(max_length=500)
#    
#    
    
    


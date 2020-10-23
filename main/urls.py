from django.urls import path,include
from main import views
urlpatterns = [
    path('',views.index,name='index'),
    path('addtocart/<int:pk>/<str:size>',views.add_to_cart,name='addtocart'),
    path('getcart/',views.get_cart,name='getcart'),
    path('delfromcart/<int:pk>',views.delfromcart,name='delfromcart'),
    path('getprice/',views.getprice,name='getprice'),
    path('category/<slug>',views.category,name='category'),
    path('category/<slug>/<int:pk>',views.item,name='item'),
#    path('mail/',views.mail , name = 'mail'),
    path('order/', views.order, name='order'),
    path('getsum/',views.getsum,name='getsum')
    # path('product/<int:pk>',views.product,name='product'),
]
#yeezy-boost-500
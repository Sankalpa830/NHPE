from django.urls import path
from store.views import Orders, Checkout, Cart, Index, Description #,Rate 
from store.views import Index, Cart, Description 
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('orders',  Orders.as_view(), name='orders'),
    path('description/<int:pid>', Description.as_view(), name='description'),
    
    #path('rate/',Rate, name='rate')
]

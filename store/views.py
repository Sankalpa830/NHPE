from django.shortcuts import render, redirect
from accounts.models import Customer
from django.views import View
from django.contrib.auth.hashers import make_password
from .models import Category, Product, Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password 
from django.http import HttpResponseRedirect



#
#
#
#
#
# orders view

class Orders(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'orders.html', {'orders': orders})



#
#
#
#
#
# Homepage View

class Index(View):
    def get(self, request):

        cart = request.session.get('cart')

        if not cart:
            request.session.cart = {}

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {'products': products, 'categories': categories}
        return render(request, 'home.html', data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)

            if quantity:

                if remove:

                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        return redirect('homepage')


#
#
#
#
#
#
# Checkout view

class Checkout(View):
    def post(self, request):

        if request.session.get('customer'):

            address = request.POST.get('address')
            phone = request.POST.get('phone')
            customer = request.session.get('customer')
            cart = request.session.get('cart')
            products = Product.get_product_by_id(list(cart.keys()))

            for product in products:
                print(product)
                order = Order(customer=Customer(id=customer),
                              product=product,
                              price=product.price,
                              address=address,
                              phone=phone,
                              quantity=cart.get(str(product.id))
                              )
                order.placeOrder()

            request.session['cart'] = {}

            return redirect('cart')

        else:
            return redirect('login')


#
#
#
#
# Cart view

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        if cart:
            ids = list(request.session.get('cart'))
            products = Product.get_product_by_id(ids)
            return render(request, 'cart.html', {'products': products})
        else:
            error_message = " Your Cart is Empty. "
            data = {
                'error': error_message
            }
            return render (request,'cart.html', data)


class Description(View):
    def post(self, request, pid):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        
        return HttpResponseRedirect(request.path_info)

    def get(self, request, pid):
        product = Product.objects.filter(id=pid)
        print(product)
        return render(request, 'description.html', {'product': product[0]})




        


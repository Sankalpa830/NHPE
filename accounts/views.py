from django.shortcuts import render, redirect
from accounts.models import Customer
from django.views import View
from django.contrib.auth.hashers import make_password
from store.models import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password


# Signup View
class SignUp(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        contact_number = request.POST.get('contactnumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'contact_number': contact_number,
            'email': email
        }

        error_message = None
        
        customer = Customer(first_name=first_name, last_name=last_name, contact_number=contact_number, email=email,
                            password=password)

        error_message = self.validateCustomer(customer)
        
        if not error_message:
            
            if not password == c_password:
                data = {
                    'error': "Password not Matched",
                    'values': value
                }
                return render(request, 'signup.html', data)
            else:    
                # saving users
                customer.password = make_password(customer.password)

                customer.save()

                return redirect('login')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):

        error_message = None
        # validation
        if not customer.first_name:
            error_message = "First Name is required"
        elif len(customer.first_name) < 2:
            error_message = "First Name must be at least 3 characters long"
        elif not customer.last_name:
            error_message = "Last Name is required"
        elif len(customer.last_name) < 2:
            error_message = "Last Name must be at least 3 characters long"
        elif not customer.contact_number:
            error_message = "Contact Number is required"
        elif len(customer.contact_number) < 10:
            error_message = "Contact Number must be at least 10 characters long"
        elif not customer.password:
            error_message = "Password is required"
        elif not customer.email:
            error_message = "Email is required"
        elif len(customer.password) < 8:
            error_message = "Password must be at least 8 characters long"
        elif len(customer.email) < 5:
            error_message = "Email must be at least 5 characters long"
        elif customer.isExists():
            error_message = "Customer address already exists"

        return error_message


#
#
#
#
#
# login view

class Login(View):
    def get(self, request):

        return render(request, 'login.html')

    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        error_message = None

        if customer:
            pwd = check_password(password, customer.password)
            if pwd:

                request.session['customer'] = customer.id
                request.session['name'] = customer.first_name
                
                return redirect('homepage')
            else:

                error_message = "Email or Password is invalid!!"

        else:
            error_message = "Email or Password is invalid!!"

        return render(request, 'login.html', {'error': error_message})


def Logout(request):
    request.session.clear()
    return redirect('login')


class Purchased_View(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'purchased.html', {'orders': orders})

class Profile_View(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        id = request.session.get('customer')
        cust_obj = Customer.objects.get(id = id)
        return render(request, 'profile.html',{'cust':cust_obj})

class EditProfile_View(View):
    def get(self,request):
        id = request.session.get('customer')
        cust_obj = Customer.objects.get(id = id)
        return render(request, 'editProfile.html',{'cust':cust_obj})

    def post(self, request):

        id = request.session.get('customer')
        cust_obj = Customer.objects.get(id = id)

        cust_obj.first_name = request.POST.get('firstname')
        cust_obj.last_name = request.POST.get('lastname')
        cust_obj.contact_number = request.POST.get('contactnumber')
        cust_obj.email = request.POST.get('email')

        cust_obj.save()
        
        return redirect('profile')

        

    

    
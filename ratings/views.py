from django.shortcuts import render
from django.http import JsonResponse
from store.models import Product
from accounts.models import Customer
from django.views import View
from .models import Rating
from django.http import HttpResponseRedirect


# Create your views here.
#
#
#
# Rate View


class Rating_View(View):
    
    def post(self, request):
        el_id = request.POST.get('el_id')
        product = Product.objects.get(id = el_id)
        val = request.POST.get('val')
        customer = request.session.get('customer')     
        rate_customer = Customer.objects.get(id = customer)

        rating = Rating( 
            customer=rate_customer,
            product=product,
            score = val
            )
        rating.save() 
        return JsonResponse({'success':'true','score':val},safe=False)
        return redirect ('homepage')
    
       
class Rate_Page(View):

    def get(self, request, pid):
        product = Product.objects.filter(id=pid)
        print(product)
        return render(request, 'rating.html', {'product': product[0]})






# def Rate(request):
#     if request.method == 'POST':   
#         el_id = request.POST.get('el_id')
#         val = request.POST.get('val')
#         obj = Rating.objects.get(id = el_id)
#         obj.score = val
#         obj.customer = 
#         obj.save()
#         return JsonResponse({'success':'true','score':val},safe=False)
#     return JsonResponse({'success':'false'})


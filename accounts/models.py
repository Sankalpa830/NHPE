from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            False

    def __str__(self):
        return self.first_name
            
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     is_customer = models.BooleanField(default=False)
#     is_vendor = models.BooleanField(default=False)

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)

#     def __str__(self):
#         return self.user.username
    
    
    # @staticmethod
    # def get_customer_by_email(email):
    #     try:
    #         return Customer.objects.get(email=email)
    #     except:
    #         return False

    # def isExists(self):
    #     if Customer.objects.filter(email=self.email):
    #         return True
    #     else:
    #         False
        
from django.db import models
from accounts.models import Customer
from store.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Rating(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ])
    def __str__(self):
        return  str(self.pk)
    
    def rateProduct(self):
        self.save()

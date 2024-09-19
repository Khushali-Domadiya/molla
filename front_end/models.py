from django.db import models
from django.forms import ModelForm
from admin_side.models import *

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    image = models.FileField(upload_to='./user_profile',default='')

class SIGNUP(ModelForm):
    class Meta:
        model = signup
        fields = "__all__"

class CART(models.Model):
    user_id = models.ForeignKey(signup,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.BigIntegerField()
    prize = models.BigIntegerField()
    sub_total = models.BigIntegerField()

class WISHLIST(models.Model):
    user_id = models.ForeignKey(signup,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.BigIntegerField()
    prize = models.BigIntegerField()
    sub_total = models.BigIntegerField()
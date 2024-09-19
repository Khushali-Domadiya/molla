from django.db import models
from django.forms import ModelForm
# Create your models here.
class sign_up(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    image = models.FileField(upload_to="./sign_up_profile/", default="")


class SIGN_UP(ModelForm):
    class Meta:
        model = sign_up
        fields = "__all__"

class slide(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)
    image = models.FileField(upload_to='./slide',default='')
    def __str__(self) -> str:
        return self.name

class SLIDE(ModelForm):
    class Meta :
        model = slide
        fields = "__all__"
        
class brand(models.Model):
    brand_name = models.CharField(max_length=200)
    image = models.FileField(upload_to='./brand',default='')
    def __str__(self) -> str:
        return self.brand_name

class BRAND(ModelForm):
    class Meta:
        model = brand
        fields = "__all__"

class category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.category_name

class CATEGORY(ModelForm):
    class Meta :
        model = category
        fields = "__all__"

class sub_category(models.Model):
    category_name = models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50)
    image = models.FileField(upload_to='./subcategory',default='')
    def __str__(self) -> str:
        return self.subcategory_name

class SUB_CATEGORY(ModelForm):
    class Meta :
        model = sub_category
        fields = "__all__"

class product(models.Model):
    name = models.CharField(max_length=50)
    brand_name = models.ForeignKey(brand,on_delete=models.CASCADE)
    category_name = models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory_name = models.ForeignKey(sub_category,on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    prize = models.CharField(max_length=20)
    image = models.FileField(upload_to='./product',default="")
    for_whom = models.CharField(max_length=20)
    

class PRODUCT(ModelForm):
    class Meta:
        model = product
        fields = "__all__"


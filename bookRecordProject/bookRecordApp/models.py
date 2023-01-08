from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type
    
    # __str__ ---> これがあったら、選択画面でCategory object(1)とかではなく、typeそのものが表示される。

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True , blank = True)
    read = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=30)
    description = models.TextField(null = True, blank = True)
    createDate = models.DateField(auto_now_add=True)
    image = models.ImageField(height_field=200,width_field=150,null=True,blank=True)
    imageUrl = models.CharField(max_length=300,null=True,blank=True)
    buy = models.BooleanField(default=False)
    review = models.TextField(null = True, blank = True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE,default=None,null=True,blank=True)
    
        

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['buy']


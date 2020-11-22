from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment = models.TextField()
    image = models.ImageField(upload_to='products', null=True)
    created_at = models.DateTimeField()
    brand = models.TextField(default='brandname')
    productname = models.TextField(default='productname')
    price = models.TextField(default='price')
    site = models.TextField(default='site')


    producttype = models.TextField(default='상품구분')
    category_m = models.TextField(default='카테고리')
    style_m = models.TextField(default='style')
    color = models.TextField(default='color')
    season = models.TextField(default='season')
    rating = models.TextField(default='별점')



    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.comment}'
            
        return f'{self.comment}'
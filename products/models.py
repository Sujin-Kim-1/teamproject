from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='products', null=True)
    created_at = models.DateTimeField()
    
    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
            
        return f'{self.body}'

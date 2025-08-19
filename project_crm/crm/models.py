from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    fullname = models.CharField(max_length=70)
    email = models.EmailField(max_length=40, null=False, unique=True)
    mobile = models.IntegerField(null=False, unique=True)
    address = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname

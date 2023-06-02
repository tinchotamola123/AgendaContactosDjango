from typing import Any
from django.db import models

# Create your models here.

class Contact(models.Model):
    avatar =    models.ImageField(upload_to='contact', null=True,blank=True)
    name =      models.CharField(max_length=100)
    email =     models.EmailField(max_length=100)
    birth =     models.DateField(null=True, blank=True)
    phone =     models.CharField(max_length=15, null=True, blank=True)
    created =   models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
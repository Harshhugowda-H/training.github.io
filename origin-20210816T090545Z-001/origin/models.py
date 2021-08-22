from django.db import models as mo


# Create your models here.
class contact_data(mo.Model):
    name = mo.CharField(max_length=15, default='')
    phone = mo.CharField(max_length=10, default='')
    email=mo.EmailField(max_length=30,default='')
    msg=mo.TextField(max_length=150,default='')

    def __str__(self):
        return self.name

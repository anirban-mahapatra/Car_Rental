from django.db import models

# Create your models here.
class UserDetail(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Contct(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    content=models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class DriverDetail(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    license=models.CharField(max_length=10)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.email
    

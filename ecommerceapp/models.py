from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='store/images')

    def __str__(self):
        return self.product_name

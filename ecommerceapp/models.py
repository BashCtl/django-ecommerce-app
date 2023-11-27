from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    description=models.CharField(max_length=500)
    phone_number=models.CharField(max_length=15)

    def __str__(self):
        return f"Contact(name={self.name}, email={self.email})"
from django.db import models
from datetime import datetime, timedelta

def get_deadline():
    return datetime.today() + timedelta(days=42)

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Job(models.Model):
    TYPE_CHOICES = [
    ("T", "Tree"),
    ("H", "Hedge"),
    ("M", "Mixed"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    description = models.TextField()
    price = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    deadline = models.DateField(default=get_deadline)
    completed = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.street + " " + self.town

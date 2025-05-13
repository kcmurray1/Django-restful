from django.db import models
from django.contrib.auth.models import User # User table is created by Django automatically

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    industry = models.CharField(max_length=20)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="customers"
    )

    def __str__(self):
        return f'{self.name} - {self.industry} owned by {self.owner}'
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
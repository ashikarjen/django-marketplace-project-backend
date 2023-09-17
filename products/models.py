from django.db import models
from django.contrib.auth.models import User
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller_phone = models.CharField(max_length=15)
    seller = models.ForeignKey(
        User,
        null=True,
        editable=False,
        on_delete=models.SET_NULL,
        related_name='products',
    )

    def __str__(self):
        return self.name
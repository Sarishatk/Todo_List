from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo_track(models.Model):

    catergory_choice = [
        ('food','Food'),
        ('rent','rent'),
        ('shopping','shopping'),
        ('vehicle','vechicle')
    ]

    category = models.CharField(max_length=20,choices=catergory_choice)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    titile = models.CharField(max_length=20)

    date = models.DateField()

    price = models.DecimalField(max_digits=10,decimal_places=2)

    note = models.CharField(max_length=120)

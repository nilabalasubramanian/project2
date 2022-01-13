from django.db import models
category_choice=(('Oil','Oil'),
                 ('Grain','Grain'),
                 ('Cosmetics','Cosmetics'))
# Create your models here.
class Grocery(models.Model):
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=1000,choices=category_choice)
    Quantity = models.IntegerField()
    RatePerUnit=models.FloatField()
    Amount = models.FloatField()


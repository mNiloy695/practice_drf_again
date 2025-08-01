from django.db import models

# Create your models here.

class MarketModel(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    location=models.CharField(max_length=100)
    market_open=models.BooleanField(default=True,null=True)

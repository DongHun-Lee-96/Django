from django.db import models

class Product(models.Model):
    # id 자동생성
    name = models.CharField(max_length=50)
    price = models.IntegerField()
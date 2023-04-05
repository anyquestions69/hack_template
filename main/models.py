from django.db import models

class User(models.Model):
    login = models.CharField(max_length=20)
    email = models.EmailField()
    filefolder = models.FilePathField(default='/tmp')
    password = models.CharField(max_length=25)

class Category(models.Model):
    name = models.CharField(max_length=60)
    
class Section(models.Model):
    name = models.CharField(max_length=60)

class Member(models.Model):
    name = models.CharField(max_length=80)
    inn = models.IntegerField(default=12345678)
    rating= models.FloatField(default=0)
    address = models.CharField(max_length=50, default='Санкт-Петербург, ул. Пионерская, д. 26')
    max_price = models.FloatField(default=0)
    min_price = models.FloatField(default=0)
    purchase_count = models.IntegerField(default=2)
    amount_accepted = models.IntegerField(default=10)
    order_count = models.IntegerField(default=15)
    average_order_time = models.FloatField(default=1.4)

class Orders(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    seller = models.ForeignKey(Member, related_name='%(class)s_seller',  on_delete = models.CASCADE)
    members = models.ManyToManyField(Member)
    buyer = models.ForeignKey(Member, related_name='%(class)s_buyer', on_delete = models.CASCADE)
    price = models.FloatField(default=1057800.45)
    status = models.BooleanField(default=True)
    date_started = models.DateTimeField(null=True)
    date_finished = models.DateTimeField(null=True)


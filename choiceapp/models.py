from django.db import models


# Create your models here.
class Customer(models.Model):
    fullname = models.CharField(max_length=60)
    address = models.CharField(max_length=180)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=55)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=55)
    class Meta:
        db_table = "customer"

    # class Meta used to rename data_app_customer to only customer


class Pollques(models.Model):
    Question = models.TextField(max_length=280)
    cho1 = models.CharField(max_length=30)
    cho2 = models.CharField(max_length=30)
    cho3 = models.CharField(max_length=30)
    cho4 = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    t_time = models.CharField(max_length=15)
    t_date = models.CharField(max_length=20)

    class Meta:
        db_table = "poll_ques"


class Solution(models.Model):
    que_id = models.CharField(max_length=10)
    ans = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    t_time = models.CharField(max_length=15)
    t_date = models.CharField(max_length=20)
    note = models.TextField(max_length=280)

    class Meta:
        db_table = "poll_sol"
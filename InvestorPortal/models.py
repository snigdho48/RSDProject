from django.db import models
from django.contrib.auth.models import User




# class History(models.Model):
#     share =
#     ammount =
#     operation =

 

# Create your models here.
class Issue(models.Model):
    name = models.TextField(max_length=50, verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    message = models.TextField(max_length=500, verbose_name="Message")
    sub_text = models.TextField(max_length=100, blank=True, verbose_name="Subject")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} {self.created_at}'


class Buy_more(models.Model):
    name = models.TextField(max_length=50, verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    message = models.TextField(max_length=500, verbose_name="Message")
    sub_text = models.TextField(max_length=100, blank=True, verbose_name="Subject")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} {self.created_at}'


class Withdraw(models.Model):
    name = models.TextField(max_length=50, verbose_name="Requester Name")
    email = models.EmailField(verbose_name="Requester Email")
    cell = models.CharField(max_length=14, verbose_name="Phone Number")
    message = models.TextField(max_length=500, verbose_name="Message")
    sub_text = models.TextField(max_length=100, blank=True, verbose_name="Subject")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} {self.created_at}'

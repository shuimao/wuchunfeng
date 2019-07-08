from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Books(models.Model):
    bookname = models.CharField(max_length=20)
    pub_time = models.DateTimeField

    def __str__(self):
        return self.bookname


class role(models.Model):
    rolename = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    weapon = models.CharField(max_length=20)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.rolename

class BookUser(User):
    telephone = models.CharField(max_length=20)

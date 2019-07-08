from django.db import models

# Create your models here.
class Questions(models.Model):
    qut = models.CharField(max_length=30)
    createtime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.qut

class Options(models.Model):
    opt = models.CharField(max_length=30)
    num = models.IntegerField(default=0)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    def __str__(self):
        return self.opt


    
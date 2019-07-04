from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    heroname = models.CharField(max_length=30)
    herogender = models.CharField(max_length=5, choices=(('man', '男'), ('woman', '女')))
    herorate = models.CharField(max_length=10, default='one')
    herocontent = models.CharField(max_length=100)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.heroname

    def explain(self):
        return self.herocontent
    explain.short_description = '简介'
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.apps import AppConfig

class Experience(models.Model):
    title = models.CharField(max_length=200, default = "")
    Comment_1 = models.CharField(default = "", blank = True, max_length=250)
    Comment_2 = models.CharField(default = "", blank = True, max_length=250)
    Comment_3 = models.CharField(default = "", blank = True, max_length=250)
    Comment_4 = models.CharField(default = "", blank = True, max_length=250)

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experience'

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=200, default = "")
    Comment_1 = models.CharField(default = "", blank = True, max_length=250)
    Comment_2 = models.CharField(default = "", blank = True, max_length=250)
    Comment_3 = models.CharField(default = "", blank = True, max_length=250)
    Comment_4 = models.CharField(default = "", blank = True, max_length=250)
    Comment_5 = models.CharField(default = "", blank = True, max_length=250)
    Comment_6 = models.CharField(default = "", blank = True, max_length=250)
    Comment_7 = models.CharField(default = "", blank = True, max_length=250)
    Comment_8 = models.CharField(default = "", blank = True, max_length=250)
    Comment_9 = models.CharField(default = "", blank = True, max_length=250)

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.title

class Skills(models.Model):
    Comment_1 = models.CharField(default = "", blank = True, max_length=250)
    Comment_2 = models.CharField(default = "", blank = True, max_length=250)
    Comment_3 = models.CharField(default = "", blank = True, max_length=250)
    Comment_4 = models.CharField(default = "", blank = True, max_length=250)

    class Meta:
        verbose_name = 'Additional skills'
        verbose_name_plural = 'Additional skills'

    def __str__(self):
        return "Additional skills"

       



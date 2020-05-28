from django.db import models
from django import forms




# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Delve_form(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    nation_slug = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    skill_html = models.BooleanField(default=False)
    skill_php = models.BooleanField(default=False)
    skill_javascript = models.BooleanField(default=False)
    skill_python = models.BooleanField(default=False)

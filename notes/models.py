from django.db import models


# Create your models here.
class Category(models.Model):
    description = models.CharField(max_length=50, unique=True)
    priority = models.IntegerField(default=-1)

    def __str__(self):
        return self.description


class Notes(models.Model):
    information = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.information

from django.db import models

# Create your models here.


class Timemixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Categories(Timemixin):
    Category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.Category

class Books(Timemixin):
    title = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Categories)









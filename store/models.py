from django.db import models


class Publishers(models.Model):
     name = models.CharField(max_length=32)
     location = models.CharField(max_length=32)

     def __str__(self):
         return self.name


class Authors(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(slef):
        return self.first_name


class Books(models.Model):
    Title = models.CharField(max_length=32)
    Author = models.ManyToManyField(Authors)

    def __str__(slef):
        return self.Title

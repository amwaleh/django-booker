from django.db import models

class Timedatemixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Publishers(Timedatemixin):
     name = models.CharField(max_length=32)
     location = models.CharField(max_length=32)


     def __str__(self):
         return self.name


class Authors(Timedatemixin):
    firstname = models.CharField(max_length=32, unique=True)
    last_name = models.CharField(max_length=32)

    @property
    def bserialize(self):
        return {
        "name":self.firstname,
        "last":self.last_name,

        }
        return serializer
    def __str__(self):
        return self.firstname


class Books(Timedatemixin):
    Title = models.CharField(max_length=32)
    Author = models.ManyToManyField(Authors)

    def __str__(self):
        return self.Title

from django.db import models

class Employer(models.Model):
    name_of_employer = models.CharField(max_length=100);
    age = models.IntegerField(default=10);


class Person(models.Model):
    name = models.CharField(max_length=100);
    age = models.IntegerField(default=10);

    def __str__(self):
        return self.name

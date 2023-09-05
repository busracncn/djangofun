import datetime
from django.db import models

# Create your models here.

class Profession(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, blank=True, null=True)
    is_headmaster = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class House(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    head = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    
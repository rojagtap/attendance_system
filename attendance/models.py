from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.dispatch import receiver


# belongs_to, where refer to the class eg. SE COMP, BE COMP

class Class(models.Model):
    name = models.CharField(max_length=100)
    strength = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    uid = models.IntegerField()
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    address = models.TextField()
    belongs_to = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    where = models.ManyToManyField(Class)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Faculty(AbstractUser):
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Lecture(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    where = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    date = models.DateField()
    time_from = models.IntegerField()
    time_to = models.IntegerField()

    def __str__(self):
        return str(self.subject) + " " + str(self.where) + "|" + str(self.date) + "|" + str(self.time_from) + "-" + str(self.time_to)

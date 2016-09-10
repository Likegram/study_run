from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):

    nickname = models.CharField(max_length=128)


class Course(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')


class Lesson(models.Model):

    number = models.IntegerField()
    course = models.ForeignKey(Course)

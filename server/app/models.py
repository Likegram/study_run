from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):

    nickname = models.CharField(max_length=128)


class Course(models.Model):

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')
    hidden = models.BooleanField(default=False)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)

    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


class Lesson(models.Model):

    number = models.IntegerField() # for ordering
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=256)


class LessonPart(models.Model):

    number = models.IntegerField()
    lesson = models.ForeignKey(Lesson)
    title = models.CharField(max_length=256)
    text = models.TextField()


class Poll(models.Model):

    lesson_part = models.ForeignKey(LessonPart, null=True)
    lesson = models.ForeignKey(Lesson)

    question = models.CharField(max_length=256)
    answer1 = models.CharField(max_length=128)
    answer2 = models.CharField(max_length=128)
    answer3 = models.CharField(max_length=128)
    answer4 = models.CharField(max_length=128)

    true_answer_number = models.IntegerField(null=True, default=None)
    string_answer = models.CharField(max_length=128)

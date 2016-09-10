from rest_framework import serializers

from .models import Course, Lesson, LessonPart, Poll, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', )


class StudentSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'nickname')

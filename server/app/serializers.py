from rest_framework import serializers

from .models import Course, Lesson, LessonPart, Poll


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', )





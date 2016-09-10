from django.shortcuts import render

# Create your views here.

from .models import Course, Student, StudentCourse

from .serializers import CourseSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @detail_route(methods=['GET'])
    def start(self, request, pk=None):
        username = request.GET.get('username', None)
        user = Student.objects.get(nickname=username)
        course = Course.objects.get(id=pk)
        student_course, created = StudentCourse.objects.get_or_create(student=user, course=course)
        StudentCourse.objects.filter(student=user).update(active=False)
        student_course.active = True
        student_course.save()
        return Response({'success': True})

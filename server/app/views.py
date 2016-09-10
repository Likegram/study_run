from django.shortcuts import render

# Create your views here.

from .models import Course, Student, StudentCourse

from .serializers import CourseSerializer, StudentSerialiser
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialiser

    @list_route(methods=['GET'])
    def make(self, request):
        username = request.GET.get('username', None)
        if username:
            Student.objects.get_or_create(nickname=username)
        return Response({'success': True})


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        result = super(CourseViewSet, self).get_queryset()

        username = self.request.GET.get('username', None)
        active = self.request.GET.get('active', None)

        if not username or active != '1':
            return result

        user = Student.objects.get(nickname=username)
        courses_ids = StudentCourse.objects.filter(student=user, active=True).values_list('course_id', flat=True)
        return result.filter(id__in=courses_ids)

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

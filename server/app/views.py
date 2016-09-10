from django.shortcuts import render

# Create your views here.

from .models import Course

from .serializers import CourseSerializer
from rest_framework import routers, serializers, viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer





from rest_framework import routers
from .views import CourseViewSet, StudentViewSet


router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'student', StudentViewSet)

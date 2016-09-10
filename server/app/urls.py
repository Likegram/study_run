from django.conf.urls import url, include
from .routers import router

# from .views import start_course


urlpatterns = [

    url(r'^', include(router.urls)),
    # url(r'^api/course/start/$', start_course),

]

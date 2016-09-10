from django.contrib import admin

from .models import Student, Course, Lesson, LessonPart, Poll

# Register your models here.

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonPart)
admin.site.register(Poll)

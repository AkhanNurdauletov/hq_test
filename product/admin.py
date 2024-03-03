from django.contrib import admin
from .models import Course, Subject, Student, Group, Membership

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Membership)


# Register your models here.

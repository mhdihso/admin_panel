from django.contrib import admin
from .models import *

admin.site.register(Field)
admin.site.register(Lesson)
admin.site.register(Grade)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Category)
admin.site.register(Course)
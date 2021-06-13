from  django_filters import FilterSet ,  NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from  . import models

class QuestionFilterSet(FilterSet):
    field = NumberFilter(field_name='lessons__course__grade__field')
    grade = NumberFilter(field_name='lessons__course__grade')
    lessons = NumberFilter(field_name='lessons')
    category = NumberFilter(field_name='category')
    author = NumberFilter(field_name='author')
    hardness = NumberFilter(field_name='hardness')
    type = NumberFilter(field_name='type')
    course = NumberFilter(field_name='lessons__course')

    class Meta:
        model = models.Question
        fields = ['field' , 'grade' , 'lessons' , 'category' , 'author' , 'hardness' , 'type' , 'course']


class GradeFilterSet(FilterSet):
    field = NumberFilter(field_name='grade__field')

    class Meta:
        model = models.Grade
        fields = ['field']


class LessonFilterSet(FilterSet):
    field = NumberFilter(field_name='course__grade__field')
    course = NumberFilter(field_name='course')
    grade = NumberFilter(field_name='course__grade')

    class Meta:
        model = models.Lesson
        fields = ['field' , 'course' , 'grade']

class CourseFilterSet(FilterSet):
    field = NumberFilter(field_name='grade__field')
    grade = NumberFilter(field_name='grade')

    class Meta:
        model = models.Course
        fields = ['field' , 'grade']
from rest_framework import permissions as perms, response, status, generics
from . import serializers, models
from rest_framework import filters 
import random
from  django_filters import FilterSet ,  NumberFilter
from django_filters.rest_framework import DjangoFilterBackend


class ExamList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.ExamSerialaizer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Choice.objects.all()

class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.ExamSerialaizer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Choice.objects.all()


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

class QuestionList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated, ]
    serializer_class = serializers.QuestionSerializer
    filter_backends = [filters.SearchFilter , filters.OrderingFilter , DjangoFilterBackend]
    search_fields = ['^id']
    ordering_fields = ['hardness']
    filter_class = QuestionFilterSet

    def get_queryset(self):

        count = self.request.GET.get('count')
        if count:
            valid_qs_id_list = models.Question.objects.all().values_list('id', flat=True)
            random_qs_id_list = random.sample(list(valid_qs_id_list), int(count))
            queryset = models.Question.objects.filter(id__in = random_qs_id_list)
            return queryset
            
        else:
            queryset = models.Question.objects.all()
            return queryset
        
            
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.QuestionSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Question.objects.all()


class ChoiceCreate(generics.CreateAPIView):
    permission_classes = (perms.IsAuthenticated,)
    serializer_class = serializers.ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.ChoiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Choice.objects.all()
        
class FieldList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.FieldSerializer

    def get_queryset(self):
        return models.Course.objects.all()


class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.FieldSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Field.objects.all()


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.CategorySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Category.objects.all()

class GradeFilterSet(FilterSet):
    field = NumberFilter(field_name='grade__field')

    class Meta:
        model = models.Grade
        fields = ['field']

class GradeList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.GradeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = GradeFilterSet

    def get_queryset(self):
        return models.Grade.objects.all()


class GradeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.GradeSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Grade.objects.all()

class LessonFilterSet(FilterSet):
    field = NumberFilter(field_name='course__grade__field')
    course = NumberFilter(field_name='course')
    grade = NumberFilter(field_name='course__grade')

    class Meta:
        model = models.Lesson
        fields = ['field' , 'course' , 'grade']

class LessonList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = LessonFilterSet

    def get_queryset(self):
        return models.Lesson.objects.all()


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.LessonSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Lesson.objects.all()

class CourseFilterSet(FilterSet):
    field = NumberFilter(field_name='grade__field')
    grade = NumberFilter(field_name='grade')

    class Meta:
        model = models.Course
        fields = ['field' , 'grade']

class CourseList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CourseFilterSet

    def get_queryset(self):
        return models.Course.objects.all()


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.CourseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Course.objects.all()


class SourceList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.SourceSerializer

    def get_queryset(self):
        return models.Source.objects.all()


class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.SourceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Source.objects.all()
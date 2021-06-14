import random

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework import permissions as perms
from rest_framework import response, status
from rest_framework.response import Response

from . import models, permissions, serializers
from .filters import *


class QuestionList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated, permissions.QuestionAccess]
    serializer_class = serializers.QuestionSerializer
    filter_backends = [filters.SearchFilter , filters.OrderingFilter , DjangoFilterBackend]
    search_fields = ['^id']
    ordering_fields = ['hardness']
    filter_class = QuestionFilterSet

    def create(self, request, *args, **kwargs):
        question_data = request.data
        current_user = request.user
        question_data["author"] = current_user.id
        serializer = self.get_serializer(data=question_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):

        count = self.request.GET.get('count')
        if count:
            valid_qs_id_list = models.Question.objects.filter(author = self.request.user).values_list('id', flat=True)
            random_qs_id_list = random.sample(list(valid_qs_id_list), int(count))
            queryset = models.Question.objects.filter(id__in = random_qs_id_list)
            return queryset
            
        else:
            queryset = models.Question.objects.filter(author = self.request.user)
            return queryset
        
            
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated, permissions.QuestionAccess]
    serializer_class = serializers.QuestionSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Question.objects.all()


class ChoiceCreate(generics.CreateAPIView):
    permission_classes = (perms.IsAuthenticated)
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

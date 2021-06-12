from rest_framework import permissions as perms, response, status, generics
from . import serializers, models


class QuestionList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated, ]
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        lesson_id = self.request.GET.get('lesson')
        category_id = self.request.GET.get('category')
        if lesson_id and category_id:
            return models.LessonQuestion.objects.select_related('question').filter(question__category_id=category_id,
                                                                                   lesson_id=lesson_id)
        elif lesson_id:
            return models.LessonQuestion.objects.filter(lesson_id=lesson_id).select_related('question')
        elif category_id:
            return models.Question.objects.filter(category_id=category_id)
        else:
            return models.Question.objects.all()

    def list(self, request, *args, **kwargs):
        lesson_id = self.request.GET.get('lesson')
        category_id = self.request.GET.get('category')
        questions = self.get_queryset()
        page = self.paginate_queryset(questions)
        object_list = []
        if page is not None:
            for q in page:
                if (lesson_id and category_id) or lesson_id:
                    serializer = self.get_serializer_class()
                    serializer = serializer(q.question)
                    data = serializer.data
                else:
                    serializer = self.get_serializer_class()
                    serializer = serializer(q)
                    data = serializer.data
                object_list.append(data)
            return self.get_paginated_response(object_list)
        return response.Response(object_list, status=status.HTTP_200_OK)


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


class GradeList(generics.ListCreateAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.GradeSerializer

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

    def get_queryset(self):
        return models.Course.objects.all()


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [perms.IsAuthenticated]
    serializer_class = serializers.CourseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return models.Course.objects.all()
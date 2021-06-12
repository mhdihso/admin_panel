from rest_framework import serializers
from . import models


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'
        ref_name = 'question_bank'


class QuestionSerializer(serializers.ModelSerializer):
    type_obj = serializers.ReadOnlyField()
    choices = ChoiceSerializer(many=True, read_only=True)
    choice = serializers.ListField(
        child=serializers.CharField(max_length=200), write_only=True, required=False
    )

    class Meta:
        model = models.Question
        fields = '__all__'
        read_only_fields = ['number_of_uses', 'number_of_correct_answers']

    def create(self, validated_data):
        choices = None
        if 'choice' in validated_data:
            choices = validated_data.pop('choice')
        choice_answer_number = validated_data.get('choice_answer_id')
        question = models.Question.objects.create(**validated_data)
        object_list = []
        if choices:
            for c in choices:
                values = {'question': question, 'text': c}
                object_list.append(models.Choice(**values))
            if len(object_list) > 0:
                models.Choice.objects.bulk_create(object_list)
            choice = object_list[choice_answer_number - 1]
            question.choice_answer_id = choice.id
            question.save(update_fields=['choice_answer_id'])
            
        return question


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grade
        fields = '__all__'
        ref_name = 'question_bank'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Field
        fields = '__all__'
        ref_name = 'question_bank'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        ref_name = 'question_bank'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'
        ref_name = 'question_bank'

    def create(self, validated_data):
        lessons = validated_data.pop('lessons')
        question = validated_data.get('question')
        object_list = []
        for lesson in lessons:
            values = {'lesson_id': lesson, 'question': question}
            object_list.append(models.LessonQuestion(**values))
        if len(object_list) > 0:
            models.LessonQuestion.objects.bulk_create(object_list)
        return {'question': question, 'lesson': lessons}


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'
        ref_name = 'question_bank'
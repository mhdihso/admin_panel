from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
import uuid


class Source(models.Model):
    name = models.CharField(_("نام منبع"), max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("نام برچسب "), max_length=120)

    def __str__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(_("نام رشته"), max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(_("نام پایه "), max_length=100)
    field = models.ForeignKey(Field, on_delete=models.CASCADE , default='عمومی')

    def __str__(self):
        return self.name + ' - ' + str(self.field)


class Course(models.Model):
    name = models.CharField(_("نام درس"), max_length=100)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.grade)


class Lesson(models.Model):
    name = models.CharField(_("نام عبارت درسی"), max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + str(self.course)


class Question(models.Model):
    class Types(models.IntegerChoices):
        DESCRIPTIVE = 0
        MULTI_CHOICE = 1
        TRUE_FALSE = 2
        BLANK_FILL = 3

    id = models.CharField(default=uuid.uuid4, max_length=500, blank=True, unique=True , primary_key=True)
    text = models.TextField(_("متن سوال"))
    type = models.PositiveSmallIntegerField(_("نوع سوال"), choices=Types.choices, default=Types.DESCRIPTIVE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    choice_answer_id = models.PositiveIntegerField(null=True, blank=True)
    text_answer = models.TextField(_("متن جواب"), null=True, blank=True)
    question_image = models.TextField(_("تصویر سوال"), null=True, blank=True)
    question_voice = models.TextField(_("فایل صوتی سوال"), null=True, blank=True)
    answer_image = models.TextField(_("تصویر جواب"), null=True, blank=True)
    hardness = models.PositiveIntegerField(_("درجه سختی"), validators=[MinValueValidator(1), MaxValueValidator(10)])
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True)    
    source_etc = models.CharField(_("منبع غیره"), max_length=150, null=True , blank=True)
    lessons = models.ManyToManyField(Lesson)
    number_of_uses = models.IntegerField(_("تعداد استفاده"), default=0)
    number_of_correct_answers = models.IntegerField(_("تعداد جواب درست"), default=0)
    craete_at = models.DateTimeField(auto_now_add = True)

    @property
    def answer(self):
        if self.type == self.Types.MULTI_CHOICE or self.Types.TRUE_FALSE:
            return self.choice_answer_id
        else:
            return self.text_answer

    @property
    def type_obj(self):
        if self.type == 0:
            return {'id': "0", 'name': "تشریحی"}
        elif self.type == 1:
            return {'id': "1", 'name': "چند گزینه ای"}
        elif self.type == 2:
            return {'id': "2", 'name': "درست یا غلط"}
        else:
            return {'id': "3", 'name': "جای خالی"}

    def save(self, *args, **kwargs):
        if self.type == 0:
            q = 'T'
        elif  self.type == 1:
            q = 'M'
        elif  self.type == 2 :
            q = 'TF'
        else:
            q = 'B'
        self.id =  q +  '-' +str(uuid.uuid4())[:8]+str(uuid.uuid4())[7:8]+str(uuid.uuid4())[12:13]
        super(Question, self).save(*args, **kwargs)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.TextField(_("متن گزینه"))

from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.QuestionList.as_view()),
    path('question/<str:id>/', views.QuestionDetail.as_view()),
    path('choice/', views.ChoiceCreate.as_view()),
    path('choice/<int:id>/', views.ChoiceDetail.as_view()),
    path('grade/', views.GradeList.as_view()),
    path('grade/<int:id>/', views.GradeDetail.as_view()),
    path('field/', views.FieldList.as_view()),
    path('field/<int:id>/', views.FieldDetail.as_view()),
    path('lesson/', views.LessonList.as_view()),
    path('lesson/<int:id>/', views.LessonDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('category/<int:id>/', views.CategoryDetail.as_view()),
    path('course/', views.CourseList.as_view()),
    path('course/<int:id>/', views.CourseDetail.as_view()),
    path('source/', views.SourceList.as_view()),
    path('source/<int:id>/', views.SourceDetail.as_view()),
]
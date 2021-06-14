from django.urls import path
from . import views

urlpatterns = [
    path('questionـmaker/', views.Question_MakerList.as_view()),
    path('questionـmaker/<int:id>/', views.Question_MakerDetail.as_view()),

]

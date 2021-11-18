from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.QuestionList.as_view(), name='question_list'),
    path('questions/', views.QuestionList.as_view(), name='question_list'),
    path('questions/<int:pk>', views.QuestionDetail.as_view(),
         name='question_detail'),
]

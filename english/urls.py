

from django.urls import path

from . import views

urlpatterns = [
    path("", views.MainView.as_view()),
    path("lessons/", views.LessonsView.as_view()),
    path("lesson/", views.LessonView.as_view()),
]
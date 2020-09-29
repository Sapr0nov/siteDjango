from django.conf import settings
from django.db import models
from django.db.models import Q, OuterRef, Subquery, Case, When
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Accounts, Courses, Lessons, Excersices, Blocks
#from .forms import ReviewForm, RatingForm

class MainView(View):
    def get(self, request):
        model = Accounts
        accounts = Accounts.objects.all()
        return render(request, "english/main.html", {"accounts_list":accounts})


class LessonsView(ListView):
    def get(self, request):
        model = Lessons
        lessons = Lessons.objects.all()
        return render(request, "english/lessons_list.html", {"lessons_list":lessons})

class LessonView(ListView):
    def get(self, request):
        model = Lessons
        model = Accounts
        lessons = Lessons.objects.all()
        accounts = Accounts.objects.all()
        return render(request, "english/lesson.html", {"lessons_list":lessons, "accounts_list":accounts, 'req': request})

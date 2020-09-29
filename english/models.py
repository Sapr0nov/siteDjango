from django.db import models
from datetime import date

from django.urls import reverse


class Accounts(models.Model):
    """Аккаунт"""

    type = models.BooleanField("Преподаватель", default=False)
    firstName = models.CharField("Имя", max_length=30, default="John")
    lastMame = models.CharField("Фамилия", max_length=30, default="Doe")
    middleName = models.CharField("Отчество", max_length=30, default="")
    email = models.CharField("email", max_length=100, default="example@mail.ru")
    password = models.CharField("Пароль", max_length=150, default="")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.firstName + " " + self.lastMame

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунт"


class Blocks(models.Model):
    """ Упражнения """
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    type = models.PositiveSmallIntegerField("Тип блока", default=0)
    text = models.CharField("Текст", max_length=255)
    question = models.CharField("Вопрос", max_length=255)
    answer = models.CharField("Отет", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блок задания"
        verbose_name_plural = "Блоки заданий"


class Excersices(models.Model):
    """ Упражнения """
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    blocks = models.ForeignKey(Blocks, verbose_name="Блок (задание)", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Упражнение"
        verbose_name_plural = "Упражнения"


class Lessons(models.Model):
    """Урок"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    excersices = models.ForeignKey(Excersices, verbose_name="упражнение", on_delete=models.CASCADE)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Courses(models.Model):
    """Курс"""
    title = models.CharField("Название", max_length=100)
    lessons = models.ForeignKey(Lessons, verbose_name="урок", on_delete=models.CASCADE)
    url = models.SlugField(max_length=130, unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


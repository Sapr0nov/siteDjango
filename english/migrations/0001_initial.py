# Generated by Django 3.1.1 on 2020-09-29 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField(default=False, verbose_name='Преподаватель')),
                ('firstName', models.CharField(default='John', max_length=30, verbose_name='Имя')),
                ('lastMame', models.CharField(default='Doe', max_length=30, verbose_name='Фамилия')),
                ('middleName', models.CharField(default='', max_length=30, verbose_name='Отчество')),
                ('email', models.CharField(default='example@mail.ru', max_length=100, verbose_name='email')),
                ('password', models.CharField(default='', max_length=150, verbose_name='Пароль')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Аккаунт',
                'verbose_name_plural': 'Аккаунт',
            },
        ),
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('type', models.PositiveSmallIntegerField(default=0, verbose_name='Тип блока')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=255, verbose_name='Отет')),
            ],
            options={
                'verbose_name': 'Блок задания',
                'verbose_name_plural': 'Блоки заданий',
            },
        ),
        migrations.CreateModel(
            name='Excersices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('blocks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.blocks', verbose_name='Блок (задание)')),
            ],
            options={
                'verbose_name': 'Упражнение',
                'verbose_name_plural': 'Упражнения',
            },
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('excersices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.excersices', verbose_name='упражнение')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='english.lessons', verbose_name='урок')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]

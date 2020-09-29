from django.contrib import admin
from .models import Accounts, Courses, Lessons, Excersices, Blocks

admin.site.register(Accounts)
admin.site.register(Courses)
admin.site.register(Lessons)
admin.site.register(Excersices)
admin.site.register(Blocks)

# Register your models here.

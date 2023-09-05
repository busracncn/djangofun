from django.contrib import admin
from .models import Profession, Student, Professor, House

# Register your models here.

@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display =  ['id', 'title']
    list_filter = ['title',]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =  ['id', 'first_name', 'last_name']
    list_filter = ['first_name','last_name']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display =  ['id', 'first_name', 'last_name', 'profession', 'is_headmaster']
    list_filter = ['first_name', 'last_name', 'profession']


@admin.register(House)
class CourseAdmin(admin.ModelAdmin):
    list_display =  ['id', 'name', 'head']


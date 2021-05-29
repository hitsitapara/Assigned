from django.contrib import admin
from django.db import models
from .models import User, Task
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'join_date', 'password')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'uid', 'task_title', 'task_description', 'task_pic', 'create_time_stamp')
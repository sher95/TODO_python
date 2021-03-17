from django.contrib import admin
from .forms import TaskForm
from .models import *
# Register your models here.

admin.site.register(Task)
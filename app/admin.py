from django.contrib import admin
from .models import Store, Machine, ExerciseLog

admin.site.register(Store)
admin.site.register(Machine)
admin.site.register(ExerciseLog)
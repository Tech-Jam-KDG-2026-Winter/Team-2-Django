from django.contrib import admin
from .models import Store, Machine, ExerciseLog


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "walking_minutes", "is_nearby")
    search_fields = ("name",)


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "store", "status", "difficulty")
    list_filter = ("status", "difficulty")
    search_fields = ("name",)


@admin.register(ExerciseLog)
class ExerciseLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "minutes", "did_exercise")
    list_filter = ("did_exercise", "date")
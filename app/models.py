from django.db import models
from django.contrib.auth.models import User



class Store(models.Model):
    name = models.CharField(max_length=100)
    walking_minutes = models.IntegerField(default=5)
    distance_text = models.CharField(max_length=50, default="徒歩5分")
    is_nearby = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Machine(models.Model):
    STATUS_CHOICES = [
        ("available", "空いている"),
        ("busy", "使用中"),
    ]

    DIFFICULTY_CHOICES = [
        ("beginner", "初心者向け"),
        ("middle", "中級者向け"),
    ]

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.name


class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    minutes = models.IntegerField(default=0)
    did_exercise = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
from django.db import models

class Student(models.Model):
    # 名前を保存する（最大100文字）
    name = models.CharField(max_length=100)
    # メールアドレスを保存する
    email = models.EmailField(unique=True)
    # 作成日時（自動で入る）
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
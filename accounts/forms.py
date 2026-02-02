from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email') # ユーザーネームとメールアドレスを表示
        labels = {
            'username': 'ユーザーネーム',
            'email': 'メールアドレス（任意）',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "パスワード"
        self.fields['password1'].help_text = """
            <ul>
                <li>パスワードは最低8文字以上である必要があります。</li>
                <li>パスワードを数字だけにすることはできません。</li>
            </ul>
        """
        self.fields['password2'].label = "パスワード（確認）"
        self.fields['password2'].help_text = "確認のため、もう一度同じパスワードを入力してください。"

class LoginForm(AuthenticationForm):
    # ログイン画面の「ユーザーID」という表示を「ユーザーネーム」に上書き
    username = forms.CharField(label="ユーザーネーム", widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
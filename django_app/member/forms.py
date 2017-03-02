from django.contrib.auth.forms import UserCreationForm
from django import forms
from member.models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = (
            'username',
        )
        help_texts = {
            'username': 'test',
            'password1': 'test pw',
        }
class LoginForm(forms.Form):
    user_id = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
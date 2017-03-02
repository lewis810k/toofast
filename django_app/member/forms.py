from django.contrib.auth.forms import UserCreationForm
from django import forms
from member.models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = (
            'username',
            'name',
            'git_url',
            'phone_number',
            'git_service',
        )
        help_texts = {
            'username': 'test',
        }
class LoginForm(forms.Form):
    user_id = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from member.forms import SignUpForm, LoginForm


def signup_view(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('member:signup_view')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'member/signup.html', context)


def login_fbv(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_id']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('slack:too_fast')
            else:
                form.add_error(None, 'ID or PW incorrect')

    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'member/login.html', context)


def logout_fbv(request):
    logout(request)
    return redirect('member:login_view')


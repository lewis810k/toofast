from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from member.forms import SignUpForm, LoginForm, ChangeProfile
from member.models import MyUser
import requests
import json
from toofast import settings
def signup_view(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('slack:too_fast')
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


def profile(request):
    user = request.user.username
    my_profile = MyUser.objects.get(username=user)
    print(my_profile)
    context = {
        'profiles': my_profile
    }
    return render(request, 'member/profile.html', context)


def change_profile(request):
    if request.method == 'POST':
        form = ChangeProfile(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('member:profile_view')
    else:
        form = ChangeProfile()
    context = {
        'form': form
    }
    return render(request, 'member/change-profile.html', context)

def git_repositery(request):
    client_id = settings.config['git']['client_id']
    client_secret = settings.config['git']['client_secret']
    git_url = 'https://api.github.com/users/Gosunghyun/repos'
    # parmas = {
    #     'client_id':client_id,
    #     'client_secret':client_secret,
    # }
    r = requests.get(git_url)
    text = r.json()
    print(text)
    repogitery = []
    date_list = []
    for list in text:
        a = list['full_name']
        repogitery.append(a)

    for list in repogitery:
        git_repositery_url  ='https://api.github.com/repos/{user_repogitery}/commits' .format(
            user_repogitery=list
        )
        r = requests.get(git_repositery_url)
        text = r.json()
        c = text['commit']['author']
        date_list.append(c)
    print(date_list)
    # git_sha = 'https://api.github.com/repos/{user_repogitery}/git/refs/heads/master'.format(
    #     user_repogitery=repogitery[0]
    # )
    # r = requests.get(git_sha)
    # text = r.json()
    # sha = text['object']['sha']
    # print(sha)
    # for i in repogitery:
    #     git_sha = 'https://api.github.com/repos/{user_repogitery}/git/refs/heads/master'.format(
    #         user_repogitery=i
    #     )
    #     r = requests.get(git_sha)
    #     text = r.json()
    #     try:
    #         a = text['object']['sha']
    #     except KeyError:
    #         pass
    #     print(a)
    #     sha_list.append(a)
    # print(sha_list)



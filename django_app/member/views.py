import datetime
import re

import requests
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from member.forms import SignUpForm, LoginForm, ChangeProfile
from member.models import MyUser
from toofast import settings
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


def send(to_sender):
    api_key = settings.config['sms']['api_key']
    api_secret = settings.config['sms']['api_secret']
    sender = settings.config['sms']['sender_number']
    ##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP

    # set api key, api secret
    api_key = api_key
    api_secret = api_secret

    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
    params['to'] = to_sender  # Recipients Number '01000000000,01000000001'
    params['from'] = sender  # Sender number
    params['text'] = '커밋하세요'  # Message

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])

        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)

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
        print('fdsafds')
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
    # client_id = settings.config['git']['client_id']
    # client_secret = settings.config['git']['client_secret']
    users = MyUser.objects.filter(git_service='1')

    sms_list = []
    for user in users:
        git_url = 'https://api.github.com/users/{git_name}/repos'.format(
            git_name=user.git_id
        )
        # /rate_limit << 시간체크
        # users/Gosunghyun/reposusers/Gosunghyun/repos
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
        print(repogitery)
        for list in repogitery:
            git_repositery_url = 'https://api.github.com/repos/{user_repogitery}/commits'.format(
                user_repogitery=list
            )
            r = requests.get(git_repositery_url)
            text = r.json()
            try:
                date = text[0]['commit']['author']['date']

            except KeyError:
                print('repo : {}'.format(text))
            else:
                date_list.append(date)
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        # newtime = ['2017-03-03T04:26:45Z','2017-02-29T04:26:45Z','2017-01-03T04:26:45Z','2017-07-02T04:26:45Z','2017-03-03T04:26:45Z']
        # flag = False
        # for i in date_list:
        #     datenow = re.sub(r'(\d[^T]+).*', r'\1', i)
        #     if nowDate == datenow:
        #         flag = True
        #         break
        # if flag == False:
        sms_list.append(user.phone_number)
    length = len(sms_list)
    if length == 0:
        pass
    else:
        for i in sms_list:
            send(i)
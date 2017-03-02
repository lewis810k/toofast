from django.shortcuts import redirect, render
from django.utils import timezone
from slacker import Slacker

from member.models import MyUser
from toofast.settings import config


def too_fast_view(request):
    user = MyUser.objects.get(username=request.user)
    if request.method == 'POST':
        user.fast_check = request.POST['fast_check']
        user.fast_check_time = timezone.now()
        user.save()
        counts = MyUser.objects.filter(fast_check='1').count()
        if counts >= 2:
            MyUser.objects.all().update(fast_check='0')
            # 문자보내기
            print("문자보냄!!")
            token = config['slack']['my_token']
            slack = Slacker(token)
            slack.chat.post_message('U3Q05LN4C', '테스트으으으')

        return redirect('slack:too_fast')

    users = MyUser.objects.all()
    count_users = MyUser.objects.filter(fast_check='1')
    for user in count_users:
        if user.fast_check_time:
            time = user.fast_check_time
            time_diff = (timezone.now() - time).seconds
            if time_diff > 30:
                user.fast_check = 0
                user.save()

    count = MyUser.objects.filter(fast_check='1').count()
    context = {
        'users': users,
        'count': count,
    }

    return render(request, 'slack/too_fast.html', context)

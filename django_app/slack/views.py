from django.shortcuts import render, redirect

from member.models import MyUser


def too_fast_view(request):
    if request.method == 'POST':
        user = MyUser.objects.get(username=request.user)
        print(user.fast_check)
        user.fast_check = request.POST['fast_check']
        user.save()
        print(user.fast_check)
        return redirect('slack:too_fast')

    users = MyUser.objects.all()
    context ={
        'users': users,
    }

    return render(request, 'slack/too_fast.html', context)

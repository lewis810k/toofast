from django.shortcuts import render, redirect

from member.models import MyUser

def too_fast_view(request):
    if request.method == 'POST':
        user = MyUser.objects.get(username=request.user)
        user.fast_check = request.POST['fast_check']
        user.save()
        return redirect('slack:too_fast')

    users = MyUser.objects.all()
    count = MyUser.objects.filter(fast_check='1').count()
    context ={
        'users': users,
        'count': count,
    }

    return render(request, 'slack/too_fast.html', context)

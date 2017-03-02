from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    return redirect('member:login_view')

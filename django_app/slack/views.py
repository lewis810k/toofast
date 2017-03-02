from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_group_list_view(request):
    return HttpResponse('get_group_list_view')
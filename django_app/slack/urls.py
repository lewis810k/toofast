from django.conf.urls import url
from . import views

app_name = 'slack'
urlpatterns = [
    url(r'^too_fast/$', views.too_fast_view, name='too_fast'),
    url(r'^selector/$', views.selector_view, name='selector'),
    url(r'^one_commit/$', views.one_commit_view, name='one_commit'),
]
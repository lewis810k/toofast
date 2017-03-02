from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup_view'),
    url(r'^login/$', views.login_fbv, name='login_view'),
    url(r'^logout/$', views.logout_fbv, name='logout_view'),
]

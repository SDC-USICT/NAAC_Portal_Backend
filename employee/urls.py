from django.conf.urls import url
from . import views


app_name = "employee"

urlpatterns = [
    url(r'^$',views.school,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login/dashboard/$',views.dashboard,name='dashboard'),
]
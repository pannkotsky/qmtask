from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from market.forms import auth as auth_forms
from market import views

urlpatterns = [
    url(r'^login', auth_views.login,
        {'redirect_authenticated_user': True,
         'authentication_form': auth_forms.LoginForm},
        name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]

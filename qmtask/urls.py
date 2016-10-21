from django.conf.urls import url
from django.contrib import admin

from market import views as market_views

urlpatterns = [
    url(r'^$', market_views.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]

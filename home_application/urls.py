from django.conf.urls import url
from home_application import views

urlpatterns = [
    url(r'^hello/$', views.hello),
]
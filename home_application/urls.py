from django.conf.urls import url
from home_application import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^get_biz_data/$', views.get_biz_data),
]
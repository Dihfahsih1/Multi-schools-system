from django.urls import re_path
from schools import views


urlpatterns = [
    re_path(r'^canon/', views.web, name='index_public'),
]

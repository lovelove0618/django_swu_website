from django.conf.urls import url, include
from. import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.Blog.as_view(), name='blog'),
]



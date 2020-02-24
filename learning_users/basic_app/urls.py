from basic_app import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    # url(r'^relative/$', views.relative, name='relative'),
    path('user_login/', views.user_login, name='user_login'),
    # url(r'^other/$', views.other, name='other'),
    path('register/', views.register, name='register'),
]

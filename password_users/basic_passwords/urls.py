from django.urls import path
from basic_passwords import views

#TEMPLATE URLS
app_name='basic_passwords'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login',views.user_login,name='user_login'),
]

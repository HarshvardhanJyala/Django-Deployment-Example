
from django.urls import path, re_path as url
from app_five import views

#TEMPLATE URLS !!
app_name = 'app_five'

urlpatterns = [
    url(r'^register/$',views.register, name='register'),
    url(r'^user_login/$',views.user_login, name='user_login'),
]

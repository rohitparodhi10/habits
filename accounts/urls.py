from django.urls import path
from accounts.views import register_view, login_view, user_info, user_info_show
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('info/', user_info, name='info'),
    path('show/', user_info_show, name='show')
]

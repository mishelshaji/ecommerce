from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_authenticate, name='accounts_login'),
    path('register/', register, name='accounts_register'),
]
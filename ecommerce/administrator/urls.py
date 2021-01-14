from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='admin_home'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category/list/', CategoryListView.as_view(), name='admin_category_list'),
]
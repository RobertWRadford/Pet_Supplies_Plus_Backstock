from django.conf.urls import url
from django.urls import path, re_path

# Import all classes from the .views file
# from .views import test_map_view
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('stock/', views.stock_view, name='stock'),
]
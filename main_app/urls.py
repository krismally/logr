from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.logs_index, name='index'),
    path('dashboard/<int:log_id>/', views.logs_detail, name='detail')
]
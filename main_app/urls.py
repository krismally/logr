from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.logs_index, name='index'),
    path('dashboard/<int:log_id>/', views.logs_detail, name='detail'),
    path('dashboard/create/', views.LogCreate.as_view(), name ='logs_create'),
    path('dashboard/<int:pk>/update/', views.LogUpdate.as_view(), name ='logs_update'),
    path('dashboard/<int:pk>/delete/', views.LogDelete.as_view(), name ='logs_delete')
]
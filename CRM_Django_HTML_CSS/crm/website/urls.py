from django.urls import path
from website import views

urlpatterns = [
    path('', views.homepage, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<pk>/', views.customer_record, name='record'),
    path('delete_confirmation/<pk>/', views.delete_confirmation, name='delete_confirmation'),
    path('delete_record/<pk>/', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<pk>/', views.update_record, name='update_record'),
]
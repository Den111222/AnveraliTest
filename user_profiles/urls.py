from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('performer/', views.performer_dashboard, name='performer_dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]

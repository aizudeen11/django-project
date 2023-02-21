from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('members/portfolio/', views.portfolio, name='portfolio'),
    path('', views.home, name='home'),
    path('members/rate/', views.rate, name='rate'),
    path('members/rate/<int:id>', views.edit, name='edit'),
    path('members/delete/<int:id>', views.delete, name='delete'),
    path('test', views.test, name='test'),
    path('my_api', views.api, name='api'),
]
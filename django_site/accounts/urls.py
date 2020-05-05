from django.urls import path
from .views import login_view, logout_view, register_view, change_profile, password_change, profile

urlpatterns = [
    path('profile', profile, name='profile'),
    path('password_change', password_change, name='password_change'),
    path('change_profile', change_profile, name='change_profile'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]

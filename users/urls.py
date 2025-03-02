# urls.py - Extensions
from django.urls import path
from .views import (
    UserCreateView, LoginView, 
    UserProfileView, UserUpdateView, UserDeleteView,
    UserProfileManagementView
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile-update'),  # Endpoint: /api/users/profile/update/ ou /api/users/me/
    path('profile/delete/', UserDeleteView.as_view(), name='profile-delete'),
    
    # Ou utiliser une seule route pour gérer le profil
    path('me/', UserProfileManagementView.as_view(), name='me'),
]
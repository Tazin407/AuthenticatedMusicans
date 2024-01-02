from django.urls import path
from .import views

urlpatterns = [
    path('add_musician/',views.Add_Musician.as_view(), name='add_musician'),
    path('signup/',views.signup, name='user_signup'),
    path('login/',views.user_login, name='user_login'),
    path('logout/',views.user_logout, name='user_logout'),
]

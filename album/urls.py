from django.urls import path
from .import views

urlpatterns = [
    path('add_album/',views.Add_Album.as_view(), name='add_album'),
    path('',views.Show_Album.as_view(), name='home')
    # path('add_album/',views.add_album, name='add_album'),
]

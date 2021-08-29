from django.urls import path, include
from .import views
app_name = 'banking'

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.registerAccount, name='register',),
    path('user-details/', views.user_details, name='user_details',),
    path('transfer/', views.transfer, name="transfer"),
    path('transfer_history/', views.transfer_history, name='transfer_history'),
]

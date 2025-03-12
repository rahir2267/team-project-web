# urls.py
from django.urls import path
from monitoring.views import add_data, dashboard

urlpatterns = [
    path('add_data/', add_data, name='add_data'),
    path('dashboard/', dashboard, name='dashboard'),
]

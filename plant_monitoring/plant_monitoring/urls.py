from django.contrib import admin
from django.urls import path
from monitoring.views import add_data, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('add_data/', add_data, name='add_data'),
]

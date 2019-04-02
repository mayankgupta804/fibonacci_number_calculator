from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('fibonacci_number_calculator.urls')),
    path('admin/', admin.site.urls),
]

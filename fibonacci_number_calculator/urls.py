from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fib_calculate', views.fib_calculator, name='fib_calculator')
]
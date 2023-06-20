from django.urls import path
from facts import views

urlpatterns = [
    path('', views.home),
    path('animal', views.fun_animal_facts),
    path('capital', views.fun_capital_facts),
]
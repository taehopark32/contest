from django.urls import path
from facts import views

urlpatterns = [
    path('', views.home),
    path('animal/', views.AnimalList.as_view()),
    path('capital', views.CapitalList.as_view()),
]
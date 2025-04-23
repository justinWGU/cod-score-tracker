from django.urls import path
from . import views

urlpatterns = [
    path('get-scores/', views.get_scores),
]
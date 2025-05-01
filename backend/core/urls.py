from django.urls import path
from . import views

urlpatterns = [
    path('update-scores/', views.update_scores_view, name='update-scores'),
    path('get-scores/', views.get_scores, name='get-scores'),
]
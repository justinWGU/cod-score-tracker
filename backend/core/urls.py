from django.urls import path
from . import views

urlpatterns = [
    path('update-scores/', views.update_scores_view),
    path('update-scores-test/', views.update_scores_view_test),
    path('get-scores/', views.get_scores),
]
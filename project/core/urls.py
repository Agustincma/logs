from django.urls import path
from .views import log_analyzer

urlpatterns = [
    path('', log_analyzer, name='log_analyzer'),
]

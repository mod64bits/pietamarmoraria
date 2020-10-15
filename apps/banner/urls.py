from django.urls import path
from .views import NovoBaner

app_name = 'banner'

urlpatterns = [
    path('', NovoBaner.as_view(), name='novo-banner'),
]

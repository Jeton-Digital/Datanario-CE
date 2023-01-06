# accounts/urls.py
from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='login'),
]

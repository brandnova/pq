from django.urls import path

from . import views

app_name = 'docs'

urlpatterns = [
    path('item/<int:pk>/', views.details, name='details'),
]

from django.urls import path

from app_familia import views

urlpatterns = [
    path('', views.index),
    path('show/<int:id>', views.show)
]

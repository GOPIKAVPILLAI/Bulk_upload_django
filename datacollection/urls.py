from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view/',views.upload_images),
    path('random-image/', views.random_image_view, name='random_image'),
]
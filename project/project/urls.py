from django.contrib import admin
from django.urls import path
from predictor import views

urlpatterns = [
    path(route='',
        view=views.index,
        name=''),
    path(
        route='index/',
        view=views.index,
        name='index'
    )
]

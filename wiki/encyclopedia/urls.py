from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("randompage", views.randompage, name="randompage"),
    path("<str:title>", views.entry, name="entry"),
    path("CSS/", views.css_entry, name="css_entry"),
    path("edit/<str:title>", views.edit, name="edit"),
]

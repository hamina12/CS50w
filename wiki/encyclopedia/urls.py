from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<str:name>", views.edit, name="edit"),
    path("<str:title>", views.entry, name="entry")
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry", veiws.entry, name="entry")
]

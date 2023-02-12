from django.urls import path

from . import views

urlpatterns = [
    path("", views.upload_image, name="upload"),
    path("", views.display_image, name="display"),
    #path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

]

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("upload", views.upload_image, name="upload"),
    path("display", views.display_images, name="display"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

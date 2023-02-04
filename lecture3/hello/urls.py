from django.url import path

urlpatterns = [
    path("", views.index, name="index")
]
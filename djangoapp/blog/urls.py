from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    # blog:index
    path("", views.index, name="index"),
]

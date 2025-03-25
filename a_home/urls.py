from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("create_item/", views.create_item, name="create-item"),
]

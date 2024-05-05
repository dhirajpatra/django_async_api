# movies/urls.py
from django.urls import path,include
from .views import sync_view,async_view


# app_name = "movies"
urlpatterns = [
    path("sync_api/", sync_view),
    path("async_api/",async_view)

]

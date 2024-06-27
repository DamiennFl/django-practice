from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    # Add login and create user paths
    path("create_user/", views.create_user, name="create_user"),
    path("login/", views.login, name="login"),
]

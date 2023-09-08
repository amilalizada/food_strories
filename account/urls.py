from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import register, login, profile, logout, CustomLoginView

app_name = "account"
urlpatterns = [
    path("", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", LogoutView.as_view(), name="logout")
]

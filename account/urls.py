from django.urls import path, include
from django.conf.urls.static import static
from .views import register, login, profile, logout

app_name = "account"
urlpatterns = [
    path("", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout")
]

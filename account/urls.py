from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import register, login, profile, logout, CustomLoginView, RegisterView, ActivateView

app_name = "account"
urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path('activate/<str:uidb64>/<str:token>/', ActivateView.as_view(), name="activate"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

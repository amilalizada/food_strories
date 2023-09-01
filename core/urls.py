from django.urls import path
from core.views import home, contact, ContactCreateView

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    # path("contact/", contact, name="contact")
    path("contact/", ContactCreateView.as_view(), name="contact")

]
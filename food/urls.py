"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import home
from stories.views import recipes, get_recipe
from food import settings
from django.conf.urls.static import static
from account.views import ActivateView
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('core.urls', namespace='core')),
    # path('stories/', include('stories.urls', namespace='stories')),
    path('account/', include('account.urls', namespace='account')),
    path('', include('social_django.urls', namespace='social')),
    path('api/', include('stories.api.urls', namespace='api')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('', include('core.urls', namespace='core')),
    path('stories/', include('stories.urls', namespace='stories')),
)
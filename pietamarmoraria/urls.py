"""pietamarmoraria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from apps.home import urls as home_urls
from apps.dashboard import urls as dashboard_url
from django.conf import settings
from django.conf.urls.static import static
from apps.servicos import urls as servicos_urls
from apps.banner import urls as banner_urls


urlpatterns = [
    path('', include(home_urls)),
    path('banner/', include(banner_urls)),
    path('servicos/', include(servicos_urls)),
    path('dashboard/', include(dashboard_url)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

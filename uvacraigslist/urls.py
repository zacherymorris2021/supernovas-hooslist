"""uvacraigslist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth import logout
from marketplace import views as marketplace_view
from django.conf.urls import handler404, handler500

app_name = 'uvacraigslist'

urlpatterns = [
    path('marketplace/', include('marketplace.urls'), name='marketplace'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('auth/', include('social_django.urls', namespace='social')),
    #path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = marketplace_view.custom_404
handler500 = marketplace_view.custom_500

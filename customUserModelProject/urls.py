"""customUserModelProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from .views import AccountsHomeView, AGVAccountsHomeView, agv_landing_page
from accounts.views import UserRegisterView, login_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', agv_landing_page, name='agv_home'),
    #path('', AccountsHomeView.as_view(), name='accounts_home'),
    path('useraccounts/', include('accounts.urls', namespace='accounts')),
    path('agv-accounts/', AGVAccountsHomeView.as_view(), name='agv_accounts_home'),
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('login/', login_page, name='login_user'),
    #path('logoout/', logout_page, name='logout_user'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""reminder_app URL Configuration

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
from django.contrib import admin
from django.urls import path
from reminders.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('set_reminder/', set_reminder, name='set_reminder'),
    path('disable_reminder/<id>/', disable_reminder, name='disable_reminder'),
    path('enable_reminder/<id>/', enable_reminder, name='enable_reminder'),
    path('delete_reminder/<id>/', delete_reminder, name='delete_reminder'),
    path('modify_reminder/<id>/', modify_reminder, name='modify_reminder'),
    path('', home, name='home'),
]

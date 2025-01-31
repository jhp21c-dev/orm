"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main.views import (
    about,
    notice,
    notice1,
    notice2,
    notice3,
    contact,
    abcd,
    hojun,
    mini,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about),
    path("notice/", notice),
    path("notice/1", notice1),
    path("notice/2", notice2),
    path("notice/3", notice3),
    path("contact/", contact),
    path("a/b/c/d/", abcd),
    path("user/hojun/", hojun),
    path("user/mini/", mini),
]

"""dunns_store URL Configuration

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
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout"),
    path("profile/", views.profile, name="profile"),
    path("", views.Home.as_view(), name="home"),
    path(
        "hunting-fishing",
        views.HuntingFishing.as_view(),
        name="hunting-fishing"),
    path("beer-tobacco", views.BeerTobacco.as_view(), name="beer-tobacco"),
    path("menu", views.Menu.as_view(), name="menu"),
    path("reservation", views.MakeReservation.as_view(), name="reservation"),
    path("reserved-tables", views.ReservedTables.as_view(), name="reserved"),
    path(
        "reserved-table/<id>",
        views.ReservedTable.as_view(),
        name="reserved-table"),
    path("reservation/<id>/email", views.Email.as_view(), name="send_email")
]

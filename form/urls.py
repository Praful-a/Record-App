from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login", views.login_page, name="login"),
    path("add/", views.add, name="add"),
    path("record/", views.record, name="report"),
]

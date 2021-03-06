from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    path('logout/', views.logout, name="logout"),
    path("add/", views.add, name="add"),
    path("record/", views.record, name="report"),
    path('<slug>/edit', views.edit, name="edit"),
    path('<slug>/delete', views.delete, name="delete"),
]

from django.contrib import admin
from django.urls import path
from .views import mypageview, signupview, loginview, listview, detailview, CreateClass, logoutview, evaluationview, mypageview, rankingview

urlpatterns = [
    path("signup/", signupview, name = "signup"),
    path("login/", loginview, name = "login"),
    path("", listview, name = "list"),
    path("detail/<int:pk>/", detailview, name = "detail"),
    path("create/", CreateClass.as_view(), name = "create"),
    path("logout/", logoutview, name = "logout"),
    path("evaluation/<int:pk>", evaluationview, name = "evaluation"),
    path("mypage/<str:author>", mypageview, name = "mypage"),
    path("ranking/", rankingview, name = "ranking")
]

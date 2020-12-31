from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import AudioModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def signupview(request):
    print(request.POST.get("username_data"))
    if request.method == "POST":
        print("POST method")
        username_data = request.POST["username_data"]
        password_data = request.POST["password_data"]
        try:
            User.objects.create_user(username_data, "", password_data)
        except IntegrityError:
            return render(request, "signup.html", {"error" : "このユーザーはすでに登録されています。"} )
            
    else:
        print(User.objects.all())
    return render(request, "signup.html", {})

def loginview(request):
    if request.method == "POST":
        print("POST method")
        username_data = request.POST["username_data"]
        password_data = request.POST["password_data"]
        user = authenticate(request, username = username_data, password = password_data)
        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return redirect("login")
    return render(request, "login.html")


def listview(request):
    print("===========")
    object_list = AudioModel.objects.all().order_by("?")
    return render(request, "list.html", {"object_list": object_list})


def detailview(request, pk):
    object = AudioModel.objects.get(pk = pk)
    return render(request, "detail.html", {"object" : object})

class CreateClass(CreateView):
    template_name = "create.html"
    model = AudioModel
    fields = {"title", "author", "audio"}
    success_url = reverse_lazy("list")

def logoutview(request):
    logout(request)
    return redirect("login")

@login_required
def evaluationview(request, pk):
    post = AudioModel.objects.get(pk = pk)
    author_name = request.user.get_username() + str(request.user.id)
    if not author_name in post.iine_people:
        post.iine_people = post.iine_people + author_name
        post.iine = post.iine + 1
        post.save()
    return JsonResponse({"iine" : post.iine})

def mypageview(request, author):
    post_list = AudioModel.objects.filter(author__exact = request.user)
    return render(request, "mypage.html", {"post_list" : post_list, "author": request.user})

def rankingview(request):
    object_list = AudioModel.objects.all().order_by("iine")
    print(request.user)
    return render(request, "ranking.html", {"object_list": object_list})

    
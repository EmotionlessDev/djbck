from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib import messages
from users.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login as login_user
from users.models import User
from django.shortcuts import get_object_or_404
from users.forms import UserEditForm


def index(request):
    return render(request, "index.html")


def get1(request):
    return response.HttpResponse("GET1")


def get2(request):
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return response.JsonResponse(data)


def get3(request, number):
    if number % 2 == 0:
        return response.HttpResponse("Even")
    else:
        return response.HttpResponse("Odd")


def render_form(request):
    return render(request, "form.html")


@csrf_exempt
def post1(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        city = request.POST.get("city")
        return JsonResponse({
            "name": name,
            "age": age,
            "city": city
        })
    else:
        return HttpResponse("Invalid request method")


@csrf_exempt
def postAndGet1(request):
    if request.method == "GET":
        return response.HttpResponse("GET")
    elif request.method == "POST":
        return redirect("index")
    else:
        return response.HttpResponse("Invalid request method")


@csrf_exempt
def postAndGet2(request, username):
    person = {
        "name": username,
        "age": 30,
        "city": "New York"
    }
    if request.method == "GET":
        return response.JsonResponse(person)
    elif request.method == "POST":
        return redirect("index")
    else:
        return response.HttpResponse("Invalid request method")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
        else:
            messages.error(request, "Error creating account")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def login(request):
    email = ""

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password")

        if not User.objects.filter(email=email).exists():
            messages.error(request, "User with this Email doesn't exist.")
            return render(request, "login.html", {"email": email})

        user = User.objects.get(email=email)

        # Проверяем пароль
        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, "Incorrect Password.")
            return render(request, "login.html", {"email": email})

        login_user(request, user)

        if user.is_superuser:
            return redirect("admin:index")
        return redirect("index")

    return render(request, "login.html", {"email": email})


def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "user_detail.html", {"user": user})


def edit_user(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User information updated successfully!")
            return redirect("user_detail", username=user.username)
        else:
            messages.error(request, "Error updating user information")
    else:
        form = UserEditForm(instance=user)

    return render(request, "edit_user.html", {"form": form, "user": user})


def delete_user(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect("users_list")
    return render(request, "delete_user.html", {"user": user})


def users_list(request):
    users = User.objects.all()
    return render(request, "users_list.html", {"users": users})

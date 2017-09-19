from django.shortcuts import render, redirect;
from django.contrib import auth;
from django.http import HttpResponseRedirect
from users.models import UserProfile
from .models import *


def logout(request):
    auth.logout(request)
    return redirect('/users/login/')

def login(request):
    if request.user.is_authenticated():
        return render(request, 'auth/registered.html')
    if request.method == "GET":
        return render(request, "auth/login.html");
    elif request.method == "POST":
        username = request.POST['username'];
        password = request.POST['password'];
        # make sure the username & password is good
        user = auth.authenticate(username=username, password=password);
        if user is not None: # User was found & password matched
            if user.is_active:
                #associate the user with the session
                auth.login(request, user);
                return render(request, "auth/registered.html");
            else:
                #account disabled
                return render(request, "auth/login.html", { "warning": "Your account is disabled" });
        else:
            # bad username and password
            return render(request, "auth/login.html", { "warning": "Invalid username and or password" });

def register(request):
    if request.method == "GET":
        return render(request, "auth/register.html");
    elif request.method == "POST":
        first_name = request.POST["first_name"];
        last_name = request.POST["last_name"]
        password = request.POST["password"];
        email = request.POST["email"];
        phone_no = request.POST["phone_number"]

        # call create_user from the ORM. Make sure you call save!
        try:
            auth.models.User.objects.create_user(username = email, 
                                             first_name = first_name,
                                             last_name = last_name,
                                             email = email,
                                            password=password).save();
        except:
            HttpResponseRedirect('/register')
        user = User.objects.get(username = email)
        userprofile = UserProfile(user = user, phone_no = phone_no)
        userprofile.save()
        return HttpResponseRedirect("/users/login")

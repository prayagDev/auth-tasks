from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from .forms import SignupForm, EditProfileForm, AdminEditProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def signup_user(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            # print(fm.cleaned_data)
            # print(fm.cleaned_data["username"])
            # print(fm.cleaned_data["password1"])
            # print(fm.cleaned_data["password2"])
            fm.save()
            print("done")
    else:
        fm=UserCreationForm()
    return render(request, "signup.html", {"form":fm})

def signup_user2(request):
    if request.method=="POST":
        fm=SignupForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            print(fm.cleaned_data["username"])
            print(fm.cleaned_data["password1"])
            print(fm.cleaned_data["password2"])
            fm.save()
            print("done")
    else:
        fm=SignupForm()
    return render(request, "signup.html", {"form":fm})

def login_user(request):
    if request.method=="POST":
        print(request)
        #request=request ... optional
        fm=AuthenticationForm(request, data=request.POST)
        print(request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            pwd=fm.cleaned_data['password']
            #request is totally optional!
            user=authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                print("done")
    else:
        fm=AuthenticationForm()
    return render(request, "login.html", {"form":fm})

def changepass(request):
    if request.method=="POST":
        #we'd write like this way too-
        #user=request.user, data=request.POST
        fm=PasswordChangeForm(request.user, request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user) #prevent auto log out
            print("changed")
    else:
        #user=request.user
        fm=PasswordChangeForm(request.user)
        print(request.user)
    return render(request, "changepass.html", {"form":fm})

def changepass2(request):
    if request.method=="POST":
        #we'd write like this way too-
        #user=request.user, data=request.POST
        fm=SetPasswordForm(request.user, request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user) #prevent auto log out
            print("changed")
    else:
        fm=SetPasswordForm(request.user)
        print(request.user)
    return render(request, "changepass2.html", {"form":fm})

def profilechange(request):
    if request.method=="POST":
        #we'd write like this way too-
        #user=request.user, data=request.POST
        fm=UserChangeForm()
        if fm.is_valid():
            fm.save()
            print("changed")
    else:
        fm=UserChangeForm(instance=request.user)
        print(request.user)
    return render(request, "profilechange.html", {"form":fm})

def profilechange2(request):
    if request.method=="POST":
        fm=EditProfileForm(request.POST, instance=request.user)
        if fm.is_valid():
            fm.save()
            print("changed")
    else:
        fm=EditProfileForm(instance=request.user)
        print(request.user)
    return render(request, "pc2.html", {"form":fm})

def profilechange3(request):
    if request.user.is_superuser:
        if request.method=="POST":
            fm=AdminEditProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                print("changed")
        else:
            fm=AdminEditProfileForm(instance=request.user)
            print(request.user)
    else:
        return redirect("/profilechange2")
    return render(request, "pc2.html", {"form":fm})
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate,login
# Create your views here.


def home(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/admin")
        else:
            return render(request, 'login.html')
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect('/login')

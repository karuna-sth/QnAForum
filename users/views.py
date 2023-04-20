from django.shortcuts import render

# Create your views here.

def login(request):
    context = {'page':'Login'}
    return render(request, "users/login.html", context)


def register(request):
    context = {'page':'Register'}
    return render(request, "users/register.html", context)
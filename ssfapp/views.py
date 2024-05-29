from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.
def home(request):
    return render(request, '',)

#adding the login view function
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render (request, 'base.html')
                else:
                    return HttpResponse ("Disabled account")
            else:
                return HttpResponse ("Invalid login")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return render(request, 'account/logout.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.messages import info,error
from django.contrib.auth import logout as auth_logout
from user.forms import UserCreationForm
from user.models import MyUserManager


def index(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard_index.html')
    return login(request)


def web_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    else:
        if request.method == 'POST':
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = authenticate(username=email, password=password)
            if request.POST.get('remember_me', 'off') == 'on':
                request.session.set_expiry(1209600) # 2 weeks
            else:
                request.session.set_expiry(0)
            if user is not None:
                login(request, user)
            else:
                error(request, "Invalid user password.")
        return render(request, 'registration/login.html')



def logout(request, next_page=None):
    auth_logout(request)
    if next_page:
        return redirect(next_page)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            form.save(commit=True)
            info(request, "Registration Complete Please Login To Continue.")
            return render(request, 'registration/login.html')
        return render(request, 'registration/register.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'registration/register.html' , {'form': form})

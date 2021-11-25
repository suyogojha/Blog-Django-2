from django.shortcuts import redirect, render, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import profile
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class UserLoginview(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm
    
    def get_success_url(self):
        return reverse("blogapp:blogapp")


class usersignupview(CreateView):
    template_name = "signup.html"
    model = User
    form_class = UserCreationForm
    
    def get_success_url(self):
        return reverse("userprofile:login")


def form_valid(self,form):
    super().form_valid(form)
    user = authenticate(username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password1'))
    login(self.request,user)
    return redirect(reverse("blogapp:blogapp"))


def logout_view(request):
    logout(request)
    return redirect(reverse("blogapp:blogapp"))




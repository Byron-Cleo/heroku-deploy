from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView,CreateView, FormView
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe

from .forms import UserRegistrationForm, UserLoginForm


# Create your views here.

class UserAccountsHomeView(TemplateView):
    template_name = "accounts/user_accounts_homepage.html"



class UserRegisterView(CreateView):
        form_class = UserRegistrationForm
        template_name = 'accounts/register.html'
        success_url = '/login/'


def login_page(request):
    form = UserLoginForm(request.POST or None)
    context = {
        "form": form
    }
    # next_ = request.GET.get('next')
    # next_post = request.POST.get('next')
    # redirect_path = next_ or next_post or None
    if form.is_valid():
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Error Byron")

    return render(request, "accounts/login.html", context)


# def logout_page(request):
#     logout(request)
#     return render(request, )
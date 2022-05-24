from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView
from core.models import *
from .forms import *
from resturent.models import *

# Create your views here.


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        resturent = Resturent.objects.all()
        context = {'resturent': resturent }
        return context


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    initial = {'key': 'value'}
    template_name = 'core/user_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + email)
            return redirect('core:user-login')
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    form_class = UserLogin
    initial = {'key': 'value'}
    template_name = 'core/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.info(request, 'Username OR Password is Incorrect')
        return render(request, 'core/login.html', {'form': form})


def UserLogout(request):
    logout(request)
    return redirect('core:user-login')

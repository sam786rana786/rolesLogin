from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import login, logout, authenticate
from accounts.forms import (
    RegistrationForm,
    AccountAuthenticationForm,
    AccountsUpdateForm
)
from accounts.models import Account


def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context = {'form': form}
    else:
        form = RegistrationForm()
        context = {
            'form': form
        }
    return render(request, 'register.html', context)


def loginPage(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AccountAuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def home(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'accounts/home.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.POST:
        form = AccountsUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
    else:
        form = AccountsUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "name": request.user.name,
                "work_line": request.user.work_line,
                "skills": request.user.skills,
                "profession": request.user.profession,
                "phone": request.user.phone
            }
        )
    context = {'form': form}
    return render(request, 'accounts/account.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')

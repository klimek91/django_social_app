from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakonczyło sie sukcesem.')
                else:
                    return HttpResponse("Konto jest zablokowane \ nieaktywne!")
            else:
                return HttpResponse("Nieprawidlowe dane uwierzytelniajace.")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False) #utworzenie nowego obiektu uzytkownika ale jezscze NIE zapisanie go w bazie danych
            new_user.set_password(user_form.cleaned_data['password']) #ustawienie wybranego hasła
            new_user.save() #zapisanie obiektu user w bazie danych
            return render(request, 'account/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})
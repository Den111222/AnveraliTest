from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bitrix24_integration.models import Contact
from .forms import RegistrationForm
from .models import UserProfile, RoleEnum


@login_required
def customer_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    performers = None
    if request.method == 'POST':
        # Если была отправлена форма, выполним поиск исполнителей
        performers_profiles = UserProfile.objects.filter(role=RoleEnum.PERFORMER.value) # Пустая строка для поиска всех исполнителей
        performers = [{"NAME": performer.user.username, "INFO": performer.contact_info} for performer in performers_profiles]
    return render(request, 'user_profiles/customer_dashboard.html', {'user_profile': user_profile, 'performers': performers})

@login_required
def performer_dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    customers = None
    if request.method == 'POST':
        # Если была отправлена форма, выполним поиск заказчиков
        customers_profiles = UserProfile.objects.filter(role=RoleEnum.CUSTOMER.value) # Пустая строка для поиска всех исполнителей
        customers = [{"NAME": customer.user.username, "INFO": customer.contact_info} for customer in customers_profiles]
    return render(request, 'user_profiles/performer_dashboard.html', {'user_profile': user_profile, 'customers': customers})

def home_view(request):
    return render(request, 'registration/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Проверяем, существует ли пользователь с таким именем пользователя
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Username is already taken. Please choose a different username.')
                return redirect('register')
            # Создаем пользователя
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            # Создаем контакт
            contact_name = form.cleaned_data['contact_name']
            contact = Contact.objects.create(name=contact_name)
            # Создаем профиль пользователя
            role = form.cleaned_data['role']
            contact_info = form.cleaned_data['contact_info']
            experience = form.cleaned_data['experience']
            profile = UserProfile.objects.create(user=user, contact=contact, role=role, contact_info=contact_info, experience=experience)
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    # После выхода из системы перенаправляем пользователя на главную страницу
    return redirect('home')


class CustomLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if user_profile.role == RoleEnum.CUSTOMER.value:
            return '/user_profiles/customer/'
        elif user_profile.role == RoleEnum.PERFORMER.value:
            return '/user_profiles/performer/'
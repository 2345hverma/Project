from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from datetime import date

from reminders.forms import UserSignUpForm, SetReminderForm
from reminders.models import Reminders


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignUpForm()

    return render(request, 'user_signup.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return LoginView.as_view(template_name='user_login.html', authentication_form=AuthenticationForm)(request)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    reminders = Reminders.objects.filter(user=request.user).order_by('-last_modified')
    for reminder in reminders:
        if reminder.date_of_reminder < date.today():
            reminder.enabled = False
            reminder.save()
    return render(request, 'home.html', {'reminders': reminders, 'today': date.today()})


@login_required
def set_reminder(request):
    if request.method == 'POST':
        form = SetReminderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        form = SetReminderForm()
    return render(request, 'set_reminder.html', {'form': form})


@login_required
def modify_reminder(request, id):
    if not Reminders.objects.filter(id=id, user=request.user):
        return redirect('home')
    if request.method == 'POST':
        form = SetReminderForm(request.POST, instance=Reminders.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SetReminderForm(instance=Reminders.objects.get(id=id))

    return render(request, 'modify_reminder.html', {'form': form})


@login_required
def disable_reminder(request, id):
    if not Reminders.objects.filter(id=id, user=request.user):
        return redirect('home')
    obj = Reminders.objects.get(id=id)
    obj.enabled = False
    obj.save()
    return redirect('home')


@login_required
def delete_reminder(request, id):
    if not Reminders.objects.filter(id=id, user=request.user):
        return redirect('home')
    obj = Reminders.objects.get(id=id)
    obj.delete()
    return redirect('home')


@login_required
def enable_reminder(request, id):
    if not Reminders.objects.filter(id=id, user=request.user):
        return redirect('home')
    obj = Reminders.objects.get(id=id)
    obj.enabled = True
    obj.save()
    return redirect('home')

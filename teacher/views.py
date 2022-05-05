from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView, UpdateView, CreateView
from django.contrib.auth.views import LoginView
from .forms import ProfileForm, RegisterUserForm, AuthUserForm

from .models import Profile

from datetime import datetime, date


def homes(request):
    return render(request,'home_page.html')


def initialYearAndMonth(dateProfile):
    a = [datetime.now().year, datetime.now().month, datetime.now().day]
    if dateProfile.day > a[2]:
        a[1] -= 1
    if dateProfile.month > a[1]:
        a[0] -= 1
        a[1] += 12
    ye, mo = a[0] - dateProfile.year, a[1] - dateProfile.month
    return ye, mo


def test(request):
    if request.user.is_authenticated:
        if Profile.objects.filter(key=request.user):
            pr = Profile.objects.filter(key=request.user)

            years, mon = initialYearAndMonth(Profile.objects.get(key=request.user).date)

            return render(request, 'home_page.html', {'pr': pr, 'user': request.user, 'year': years, 'mon': mon})
        else:
            return render(request, 'home_page.html')
    else:
        return redirect('log')


class RegisterFormView(FormView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('home2')
    template_name = 'registration_page.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginViews(LoginView):
    template_name = 'registration/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home2')


class ProfileView(CreateView):
    template_name = 'add_profile.html'
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy('home2')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.key = self.request.user
        obj.first_name = self.request.user.first_name
        obj.last_name = self.request.user.last_name
        obj.save()
        return HttpResponseRedirect(self.success_url)


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile_update_page.html'
    fields = ['first_name', 'last_name', 'gender_model', 'patronymic', 'date', 'birth_date', 'job', 'work_place',
              'telephone']
    success_url = reverse_lazy('home2')

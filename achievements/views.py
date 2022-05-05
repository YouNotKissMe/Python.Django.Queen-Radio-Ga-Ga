from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView
from .form import AchievementsForm, EducationForm, ProfessionalDevelopmentForm

from .models import Achievements, Education, ProfessionalDevelopment


def delete(request, id):
    if request.user.is_authenticated:
        publication = Achievements.objects.get(id=id)

        publication.delete()
        return redirect('ach')
    else:
        return render(request, "registration/login.html")


def delete_ed(request, id):
    if request.user.is_authenticated:
        ed = Education.objects.get(id=id)
        ed.delete()
        return redirect('educate')
    else:
        return render(request, "registration/login.html")


def delete_pd(request, id):
    if request.user.is_authenticated:
        pd = ProfessionalDevelopment.objects.get(id=id)
        pd.delete()
        return redirect('pd')
    else:
        return render(request, "registration/login.html")


def achievements(request):
    if request.user.is_authenticated:
        ach = Achievements.objects.filter(key=request.user)
        return render(request, 'achievements_page.html', {'ach': ach})
    else:
        return redirect('log')


def education(request):
    if request.user.is_authenticated:
        ed = Education.objects.filter(key=request.user)
        return render(request, 'education_page.html', {'ed': ed})
    else:
        return redirect('log')


def professional_development(request):
    if request.user.is_authenticated:
        pd = ProfessionalDevelopment.objects.filter(key=request.user)
        return render(request, 'professional_development_page.html', {'pd': pd})
    else:
        return redirect('log')


class AchievementsView(CreateView):
    template_name = 'add_achievements.html'
    form_class = AchievementsForm
    model = Achievements
    success_url = reverse_lazy('ach')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.key = self.request.user
        obj.save()
        return HttpResponseRedirect(self.success_url)


class EducationView(CreateView):
    template_name = 'add_education.html'
    form_class = EducationForm
    model = EducationForm
    success_url = reverse_lazy('educate')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.key = self.request.user
        obj.save()
        return HttpResponseRedirect(self.success_url)


class ProfessionalDevelopmentView(CreateView):
    template_name = 'add_professional_development.html'
    form_class = ProfessionalDevelopmentForm
    model = ProfessionalDevelopment
    success_url = reverse_lazy('pd')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.key = self.request.user
        obj.save()
        return HttpResponseRedirect(self.success_url)


class AchievementsUpdateView(UpdateView):
    model = Achievements
    template_name = 'achievements_update_page.html'
    fields = ['name', 'achievements_type', 'the_direction_of_self_development', 'file', 'date_of_receiving']
    success_url = reverse_lazy('ach')


class EducationUpdateView(UpdateView):
    model = Education
    template_name = 'education_update_page.html'
    fields = ['level', 'faculty', 'specialization', 'educational_organization', 'date']
    success_url = reverse_lazy('educate')


class ProfessionalDevelopmentUpdateView(UpdateView):
    model = ProfessionalDevelopment
    template_name = 'professional_development_update_page.html'
    fields = ['date', 'educational_organization', 'name_theme', 'number_document', 'duration_of_training',
              'number_of_hours',
              'the_direction_of_self_development']
    success_url = reverse_lazy('pd')

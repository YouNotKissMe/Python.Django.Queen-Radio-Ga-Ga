"""Curs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from teacher.views import RegisterFormView, LoginViews, test, ProfileUpdateView, ProfileView,homes
from django.contrib.auth.views import LogoutView
from achievements.views import achievements, professional_development, education, delete_pd, delete_ed, delete, \
    AchievementsView, AchievementsUpdateView, EducationView, ProfessionalDevelopmentView, \
    EducationUpdateView, ProfessionalDevelopmentUpdateView
from image.views import initImage

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('reg/', RegisterFormView.as_view(), name='reg'),
    path('log/', LoginViews.as_view(), name='log'),
    path('home/', test, name='home2'),
    path('',homes),
    path('home/ach/', achievements, name='ach'),
    path('add/', AchievementsView.as_view(), name='nerabotaet'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/ach/delete/<int:id>/', delete, name='delete'),
    path('<int:pk>/', AchievementsUpdateView.as_view(), name='update'),
    path('home/ed', education, name='educate'),
    path('added/', EducationView.as_view(), name='addeducate'),
    path('home/ed/delete/<int:id>/', delete_ed, name='delete_ed'),
    path('educate/<int:pk>/', EducationUpdateView.as_view(), name='update_ed'),
    path('home/pd/', professional_development, name='pd'),
    path('home/pd/delete/<int:id>/', delete_pd, name='delete_pd'),
    path('addpd/', ProfessionalDevelopmentView.as_view(), name='addpd'),
    path('pd/<int:pk>/', ProfessionalDevelopmentUpdateView.as_view(), name='update_pd'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='updateyou'),
    path('add_page/', ProfileView.as_view(), name='add_you'),
    path('initial/', initImage, name='initial')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

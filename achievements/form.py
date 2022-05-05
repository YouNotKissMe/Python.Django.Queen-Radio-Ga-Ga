from django.forms import ModelForm

from .models import Achievements, Education, ProfessionalDevelopment


class AchievementsForm(ModelForm):
    class Meta:
        model = Achievements
        fields = ('achievements_type', 'name', 'date_of_receiving', 'the_direction_of_self_development', 'file')


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ('level', 'educational_organization', 'faculty', 'specialization', 'date')


class ProfessionalDevelopmentForm(ModelForm):
    class Meta:
        model = ProfessionalDevelopment
        fields = (
            'date', 'educational_organization', 'name_theme', 'duration_of_training',
            'number_of_hours', 'number_document',
            'the_direction_of_self_development')

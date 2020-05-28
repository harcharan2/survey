from django import forms
from .models import Delve_form

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

class SurveyForm(forms.ModelForm):

    class Meta:
        model = Delve_form
        fields = ('name', 'email', 'country_code', 'phone', 'nation_slug', 'organization', 'position', 'skill_html', 'skill_javascript', 'skill_php', 'skill_python')
        labels = {
            'name':'Name',
            'email':'Email address',
            'country_code': 'Country code',
            'phone': 'Phone number',
            'nation_slug': 'Nation Slug',
            'organization': 'Organization',
            'position': 'Position',
            'skill_html': 'HTML',
            'skill_javascript': 'Javascript',
            'skill_php': 'PHP',
            'skill_python': 'Python'
        }

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['country_code'].required = False
        self.fields['phone'].required = False
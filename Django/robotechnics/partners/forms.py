from django import forms
from django.forms import FileInput
from partners.models import Partner


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
        widgets = {
            'photo': FileInput(
                attrs={'style':
                       'border: 1px solid #353535; '
                       'padding: 5em; border-radius: 4px'}),
        }

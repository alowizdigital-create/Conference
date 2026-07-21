from django import forms
from .models import Participant


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant

        fields = [
            'full_name',
            'local_church',
            'congregation',
            'city',
            'country',
            'quality',
            'phone',
            'photo',
        ]

        widgets = {

            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom complet'
            }),

            'local_church': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Église locale'
            }),

            'congregation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Congrégation'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ville'
            }),

            'country': forms.Select(attrs={
                'class': 'form-control'
            }),

            'quality': forms.Select(attrs={
                'class': 'form-control'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Téléphone'
            }),

            # 'photo': forms.ClearableFileInput(attrs={
            #     'class': 'form-control'
            # }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),

        }
from django import forms
from .models import Gist

class GistForm(forms.ModelForm):
    class Meta:
        model = Gist
        fields = ('title', 'text',)
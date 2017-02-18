from django import forms
from .models import Gist, Comment

class GistForm(forms.ModelForm):
    class Meta:
        model = Gist
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'text')


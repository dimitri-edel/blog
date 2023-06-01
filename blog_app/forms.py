from .models import Coment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('body',)

    
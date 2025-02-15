from django import forms
from .models import Post

class Postforms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
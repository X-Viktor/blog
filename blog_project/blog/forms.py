from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'max_length': 125}),
        required=True,
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'style': 'resize:none;'}),
        required=True,
    )

    class Meta:
        model = Post
        fields = ('title', 'description')

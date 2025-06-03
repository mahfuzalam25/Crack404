from django import forms
from .models import Post

class BlogForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'image']

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if Post.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This slug is already in use. Please choose another.")
        return slug

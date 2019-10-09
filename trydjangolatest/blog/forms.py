from django import forms
from .models import *

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'slug',
            'image',
            'content',
            'publish_date',
        ]

    # Custom Validation!!
    def clean_title(self, *args, **kwargs):
        print(dir(self))
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        query = BlogPost.objects.filter(title=title)
        if instance is not None:
            query = query.exclude(id=instance.id)
        if query.exists():
            raise forms.ValidationError('This title already exists!')
        return title
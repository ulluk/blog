from django import forms
from .models import Post, Category, Tag

# class PostForm(forms.Form):
#     image = forms.ImageField(required=False)
#     title = forms.CharField(required=True, max_length=256)
#     content = forms.CharField(required=True, max_length=456)

#     def clean_title(self):
#         cleaned_data = super().clean()
#         title = cleaned_data.get("title")
#         if title and title.lower() == 'python':
#             raise forms.ValidationError('Title cannot be Python')
#         return title
    
#     def clean(self):
#         cleaned_data = super().clean()
#         title = cleaned_data.get("title")
#         content = cleaned_data.get('content')
#         if title and title.lower() == content.lower():
#             raise forms.ValidationError('Title and content cannot be same')
#         return cleaned_data
    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class SearchForm(forms.Form):
    search = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    orderings = (
        ("rate", "Rate"),
        ("-rate", "Rate (desc)"),
        ("created_at", "Created at"),
        ("-created_at", "Created at (desc)"),
        ("updated_at", "Updated at"),
        ("-updated_at", "Updated at (desc)"),
        (None, None ),
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required =False)
from django.forms import ModelForm
from blogging.models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'posts']

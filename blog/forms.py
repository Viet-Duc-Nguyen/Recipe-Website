from djrichtextfield.widgets import RichTextWidget
from django import forms
from .models import Post, RecipeBook, Comment

class PostForm(forms.ModelForm):
    """Form to create a recipe"""

    class Meta:
        model = Post
        fields = [
            "title",
            "excerpt",
            "ingredients",
            "content",
            "image"
        ]

        widgets = {
            "ingredients": RichTextWidget(),
            "content": RichTextWidget(),
            "excerpt": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "excerpt": "Description",
            "ingredients": "Recipe Ingredients",
            "content": "Recipe Instructions",
            "image" : "Image"
        }
        
        
class UpdatePostForm(forms.ModelForm):
    """Form to update a recipe"""

    class Meta:
        model = Post
        fields = [
            "title",
            "excerpt",
            "ingredients",
            "content",
            "image"
        ]

        widgets = {
            "ingredients": RichTextWidget(),
            "content": RichTextWidget(),
            "excerpt": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "excerpt": "Description",
            "ingredients": "Recipe Ingredients",
            "content": "Recipe Instructions",
            "image" : "Image"
        }
        
############################## Recipe Book 

class RecipeBookForm(forms.ModelForm):
    
    class Meta:
        model = RecipeBook
        fields = ['title']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
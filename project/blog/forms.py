from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','body','post_image',)
        widgets={
            'title': forms.TextInput(attrs={'class':'w3-input w3-border'},),
            'body': forms.Textarea(attrs={'class':'w3-input w3-border','style':'height:140px;'},),
            'post_image': forms.ClearableFileInput(attrs={'class':'w3-button w3-border','style':'width:100%'},),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
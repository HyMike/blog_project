from django import forms
from .models import CommentsModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ['userName', 'userEmail', 'text']
        labels = {
            'userName': "Your Name",
            "userEmail": 'Your Email',
            "text": "Comment",
        }

from .models import Comment
from django import forms
from django.contrib import messages

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']

        def clean_name(self):
            name = self.cleaned_data.get('name')
            user = self.request.user 
            if(name!=user.username):
                messages.error(self.request, 'Incorrect name.')
            return name

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' }),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
    

      
from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'url', 'issue_type']

        widgets = {
            "title": forms.TextInput(attrs={'placeholder': "The title of the issue."}),
            "description": forms.Textarea(attrs=
                {"placeholder": "The issue's description. Make sure the information you put is clear and concise! "}),
            "url": forms.URLInput(),
        }
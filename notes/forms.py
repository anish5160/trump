from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'title': 'Title:',
            'text': 'Write your thoughts here:',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title[0].isupper():
            raise forms.ValidationError("The title must start with a capital letter.")
        return title

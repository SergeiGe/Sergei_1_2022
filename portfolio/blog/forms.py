from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=30,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя автора'
        })
    )
    body = forms.CharField(
        widget= forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите комментарий'
        })
    )
from typing import Any
from django import forms


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NameForm(forms.Form):
	your_name=forms.CharField(label="Your name", max_length=100)

class ContactForm(forms.Form):
	title=forms.CharField(max_length=100)
	message=forms.CharField(widget=forms.Textarea)
	sender=forms.EmailField()
	cc_myself=forms.BooleanField(required=False)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Fullname")
    class Meta:
        model = User
        fields = ("username", "fullname", "email", )
    """def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["password1"].label="Password"
        self.fields["password2"].label="Password Confirmation" """
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.fullname = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class SearchForm(forms.Form):
     search=forms.CharField(label="search", max_length=100)
     
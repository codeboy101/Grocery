from django import forms
from .models import Register

class loginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Register
		fields = ('username','password',)

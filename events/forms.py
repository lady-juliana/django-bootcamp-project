from django import forms 
from django.contrib.auth.forms import UserCreationForm
from . models import CustomUser, Event
 

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email')
 

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['title','description','date', 'image']
		widgets = {
			'date':forms.DateInput(attrs={'type':'date'}),
		}

from django import forms
from django.contrib.auth.models import User
from dog_aid.models import UserProfile, Dog, Vet, DogEvent

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
        labels = {
            "picture": "Profile Picture"
        }

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('owner', 'name', 'DOB', 'breed', 'picture')
        labels = {
            "name": "Name (first name only, one word)",
            "DOB": "Date of Birth",
            "picture": "Profile Picture"
        }

class VetForm(forms.ModelForm):
    class Meta:
        model = Vet
        fields = ('name', 'phone_number', 'address', 'type', 'dog_owner')
        labels = {
            "type": "Priority of Vet",
        }

class DogEventForm(forms.ModelForm):
    class Meta:
        model = DogEvent
        fields = ('name', 'dog', 'event_type', 'date', 'notes')
        labels = {
            'name': 'Name of Event',
            'event_type': 'Type of Event',
            'date': 'Date of Event'
        }
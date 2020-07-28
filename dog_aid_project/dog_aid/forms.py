from django import forms
from django.contrib.auth.models import User
from dog_aid.models import UserProfile, VetProfile, DogProfile, DogOwner

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class DogOwnerForm(forms.ModelForm):
    class Meta:
        model = DogOwner
        fields = ('owner_name', 'dog', 'vet')

class DogProfileForm(forms.ModelForm):
    class Meta:
        model = DogProfile
        fields = ('owner', 'dog_name', 'date_of_birth', 'breed_of_dog', 'picture')

class VetProfileForm(forms.ModelForm):
    class Meta:
        model = VetProfile
        fields = ('name_of_vet', 'phone_number', 'street', 'town', 'county', 'postcode')

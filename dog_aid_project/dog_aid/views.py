from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from dog_aid.forms import UserForm, DogProfileForm, VetProfileForm, UserProfileForm
from django.contrib.auth.models import User
from dog_aid.models import UserProfile, DogProfile
from django.utils.decorators import method_decorator
from django.views import View

def index(request):
    return render(request, 'dog_aid/index.html')

def emergency(request):
    return render(request, 'dog_aid/emergency.html')

def appointment(request):
    return render(request, 'dog_aid/appointment.html')

@login_required
def profile(request):
    return render(request, 'dog_aid/profile.html')

def illnesses(request):
    return render(request, 'dog_aid/illnesses.html')

def vet(request):
    return render(request, 'dog_aid/vet.html')

def quiz(request):
    return render(request, 'dog_aid/quiz.html')

def first(request):
    return render(request, 'dog_aid/first.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'dog_aid/registration_form.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def register_dog(request):
    dog_form = DogProfileForm()

    if request.method == 'POST':
        dog_form = DogProfileForm(request.POST, request.FILES)

        if dog_form.is_valid():
            dog_profile = dog_form.save(commit=False)
            dog_profile.save()

            return redirect(reverse('dog_aid:index'))

        else:
            print(dog_form.errors)

    context_dict = {'dog_form': dog_form}
    return render(request, 'dog_aid/profile_registration.html', context_dict)

class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserForm()
        return (user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'dog_aid/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('dog_aid:profile', user.username)
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user, 'form': form}

        return render(request, 'dog_aid/profile.html', context_dict)

class DogProfileView(View):
    def get_dog_details(self, dog_name):
        try:
            dog = DogProfile.objects.get(dog_name=dog_name)
        except dog.DoesNotExist:
            return None

        dog_profile = DogProfile.objects.get_or_create(dog=dog)[0]
        dog_form = DogProfileForm()
        return (dog, dog_profile, dog_form)

    @method_decorator(login_required)
    def get(self, request, dog_name):
        try:
            (dog, dog_profile, dog_form) = self.get_dog_details(dog_name)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        context_dict = {'dog_profile': dog_profile,
                        'selected_dog': dog,
                        'dog_form': dog_form}

        return render(request, 'dog_aid/dog_profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (dog, dog_profile, dog_form) = self.get_dog_details(dog_name)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        dog_form = DogProfileForm(request.POST, request.FILES, instance=dog_profile)
        if dog_form.is_valid():
            dog_form.save(commit=True)
            return redirect('dog_aid:dog_profile', dog.dog_name)
        else:
            print(dog_form.errors)

        context_dict = {'dog_profile': dog_profile,
                        'selected_dog': dog, 'dog_form': dog_form}

        return render(request, 'dog_aid/dog_profile.html', context_dict)

class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
        profiles = UserProfile.objects.all()
        return render(request, 'dog_aid/list_profiles.html', {'user_profile_list': profiles})

class ListDogProfiles(View):
    @method_decorator(login_required)
    def get(self, request):
        dog_profiles = DogProfile.objects.all()
        return render(request, 'dog_aid/dog_profile_list.html', {'dog_profile_list': dog_profiles})

@login_required
def registerVet(request):
    form = VetProfileForm()

    if request.method == 'POST':
        form = VetProfileForm(request.POST, request.FILES)

        if form.is_valid():
            vet_profile = form.save(commit=False)
            vet_profile.user = request.user
            vet_profile.save()

            return redirect(reverse('dog_aid:index'))

        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'dog_aid/vet_register.html', context_dict)



from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from dog_aid.forms import UserForm, DogForm, VetForm, UserProfileForm, DogEventForm
from django.contrib.auth.models import User
from dog_aid.models import UserProfile, Dog, Vet, Symptom, Illness, DogEvent
from django.utils.decorators import method_decorator
from django.views import View

def index(request):
    return render(request, 'dog_aid/index.html')

def quiz(request):
    return render(request, 'dog_aid/quiz.html')

def training(request):
    return render(request, 'dog_aid/training.html')

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

    return render(request, 'dog_aid/registration_form.html', context={'user_form': user_form,
                                                                      'profile_form': profile_form,
                                                                      'registered': registered})

@login_required
def register_dog(request):
    dog_form = DogForm()

    if request.method == 'POST':
        dog_form = DogForm(request.POST, request.FILES)

        if dog_form.is_valid():
            dog_profile = dog_form.save(commit=False)
            dog_profile.save()

            return redirect(reverse('dog_aid:index'))

        else:
            print(dog_form.errors)

    context_dict = {'dog_form': dog_form}
    return render(request, 'dog_aid/profile_registration.html', context_dict)

@login_required
def registerVet(request):
    form = VetForm()

    if request.method == 'POST':
        form = VetForm(request.POST, request.FILES)

        if form.is_valid():
            vet_profile = form.save(commit=False)
            vet_profile.user = request.user
            vet_profile.save()

            return redirect(reverse('dog_aid:index'))

        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'dog_aid/vet_register.html', context_dict)

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
    def get_dog_details(self, name):
        try:
            dog = Dog.objects.get(name=name)
        except dog.DoesNotExist:
            return None

        dog_profile = Dog.objects.get_or_create(name=name)[0]
        dog_form = DogForm()
        event_profile = DogEvent.objects.filter(dog=dog).order_by('-date')
        return (dog, dog_profile, dog_form, event_profile)

    @method_decorator(login_required)
    def get(self, request, name):
        try:
            (dog, dog_profile, dog_form, event_profile) = self.get_dog_details(name)
            event_profile = DogEvent.objects.filter(dog=dog).order_by('-date')
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        context_dict = {'dog_profile': dog_profile,
                        'selected_dog': dog,
                        'dog_form': dog_form,
                        'event': event_profile}

        return render(request, 'dog_aid/dog_profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (dog, dog_profile, dog_form, event_profile) = self.get_dog_details(name)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        dog_form = DogForm(request.POST, request.FILES, instance=dog)
        if dog_form.is_valid():
            dog_form.save(commit=True)
            return redirect('dog_aid:dog_profile', dog.name)
        else:
            print(dog_form.errors)

        context_dict = {'dog_profile': dog_profile,
                        'selected_dog': dog,
                        'dog_form': dog_form,
                        'event': event_profile}

        return render(request, 'dog_aid/dog_profile.html', context_dict)

@login_required
def registerDogEvent(request):
    event_form = DogEventForm()

    if request.method == 'POST':
        event_form = DogEventForm(request.POST, request.FILES)

        if event_form.is_valid():
            event_profile = event_form.save(commit=False)
            event_profile.save()

            return redirect(reverse('dog_aid:index'))

        else:
            print(event_form.errors)

    context_dict = {'event_form': event_form}
    return render(request, 'dog_aid/register_dog_event.html', context_dict)

class VetProfileView(View):
    def get_vet_details(self, name):
        try:
            vet = Vet.objects.get(name=name)
        except vet.DoesNotExist:
            return None

        vet_profile = Vet.objects.get_or_create(name=name)[0]
        vet_form = VetForm()
        return (vet, vet_profile, vet_form)

    @method_decorator(login_required)
    def get(self, request, name):
        try:
            (vet, vet_profile, vet_form) = self.get_vet_details(name)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        context_dict = {'vet_profile': vet_profile,
                        'selected_vet': vet,
                        'vet_form': vet_form}

        return render(request, 'dog_aid/vet_profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, name):
        try:
            (vet, vet_profile, vet_form) = self.get_vet_details(name)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        vet_form = VetForm(request.POST, request.FILES, instance=vet)
        if vet_form.is_valid():
            vet_form.save(commit=True)
            return redirect('dog_aid:vet_profile', vet.name)
        else:
            print(vet_form.errors)

        context_dict = {'vet_profile': vet_profile,
                        'selected_vet': vet, 'vet_form': vet_form}

        return render(request, 'dog_aid/vet_profile.html', context_dict)

class SymptomView(View):
    def get_symptom_details(self, name):
        try:
            symptom = Symptom.objects.get(name=name)
        except symptom.DoesNotExist:
            return None
        return symptom

    def get(self, request, name):
        try:
            symptom = self.get_symptom_details(name)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        illness_list = symptom.illness_set.all()

        context_dict = {'selected_symptom': symptom,
                        'illness_list': illness_list}

        return render(request, 'dog_aid/symptom_profile.html', context_dict)

class IllnessView(View):
    def get_illness_details(self, name):
        try:
            illness = Illness.objects.get(name=name)
        except illness.DoesNotExist:
            return None
        return illness

    def get(self, request, name):
        try:
            illness = self.get_illness_details(name)
        except TypeError:
            return redirect(reverse('dog_aid:index'))

        symptom_list = illness.related_symptom.all()

        context_dict = {'selected_illness': illness,
                        'symptom_list': symptom_list}

        return render(request, 'dog_aid/illness_profile.html', context_dict)

class ListProfilesView(View):
    @method_decorator(login_required)
    def get(self, request):
        profiles = UserProfile.objects.all()
        return render(request, 'dog_aid/list_profiles.html', {'user_profile_list': profiles})

class ListDogProfiles(View):
    @method_decorator(login_required)
    def get(self, request):
        current_user = request.user
        dog_profiles = Dog.objects.filter(owner=current_user)
        return render(request, 'dog_aid/dog_profile_list.html', {'dog_profile_list': dog_profiles})

class ListVetProfiles(View):
    @method_decorator(login_required)
    def get(self, request):
        current_user = request.user
        vet_profiles = Vet.objects.filter(dog_owner=current_user)
        return render(request, 'dog_aid/vet_list.html', {'vet_list': vet_profiles})

class ListSymptomsIllnessView(View):
    def get(self, request):
        symptom = Symptom.objects.all()
        illness = Illness.objects.all()
        return render(request, 'dog_aid/emergency.html', {'symptom_list': symptom, 'illness_list': illness})

class ListIllnessView(View):
    def get(self, request):
        illness = Illness.objects.all().order_by('name')
        return render(request, 'dog_aid/illness_all.html', {'list_illness': illness})

def get_illness_list(max_results=0, contains=''):
    illnesses = []
    if contains:
        illnesses = Illness.objects.filter(name__icontains=contains).order_by('name')
    else:
        illnesses = []
        illnesses = Illness.objects.all().order_by('name')
    return illnesses

def get_symptom_list(max_results=0, contains=''):
    symptoms = []
    if contains:
        symptoms = Symptom.objects.filter(name__icontains=contains).order_by('name')
    else:
        symptoms = []
        symptoms = Symptom.objects.all().order_by('name')
    return symptoms

def illness_suggest(request):
    illness_list = []
    symptom_list = []
    if request.method == 'GET':
        contains = request.GET['suggestion']
    illness_list = get_illness_list(8, contains)
    symptom_list = get_symptom_list(8, contains)
    return render(request, 'dog_aid/illness_suggest.html', {'illnesses': illness_list, 'symptoms': symptom_list})

def get_emergency_list(max_results=0, contains=''):
    emergency_illnesses = []
    if contains:
        emergency_illnesses = Illness.objects.filter(name__icontains=contains).order_by('name')
    else:
        emergency_illnesses = []
        emergency_illnesses = Illness.objects.all().order_by('name')
    return emergency_illnesses

def get_symptom_list(max_results=0, contains=''):
    emergency_symptoms = []
    if contains:
        emergency_symptoms = Symptom.objects.filter(name__icontains=contains).order_by('name')
    else:
        emergency_symptoms = []
        emergency_symptoms = Symptom.objects.all().order_by('name')
    return emergency_symptoms

def emergency_suggest(request):
    emergency_illness_list = []
    emergency_symptom_list = []
    if request.method == 'GET':
        contains = request.GET['emergency_suggestion']
    emergency_illness_list = get_emergency_list(8, contains)
    emergency_symptom_list = get_symptom_list(8, contains)
    return render(request, 'dog_aid/emergency_suggest.html',
                  {'emergency_illnesses': emergency_illness_list, 'emergency_symptoms': emergency_symptom_list})
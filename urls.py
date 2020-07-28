from django.urls import path
from dog_aid import views

app_name = 'dog_aid'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('emergency/', views.emergency, name='emergency'),
    path('profile/', views.profile, name='profile'),
    path('illnesses/', views.illnesses, name='illnesses'),
    path('vet/', views.vet, name='vet'),
    path('quiz/', views.quiz, name='quiz'),
    path('', views.first, name='first'),
    path('vet_register/', views.registerVet, name='vet_register'),
    #path('register_profile/', views.register_profile, name='register_profile'),
    path('register_dog/', views.register_dog, name='register_dog'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('dog_profile/<dog_name>/', views.DogProfileView.as_view(), name='dog_profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('dog_profile_list/', views.ListDogProfiles.as_view(), name='dog_profile_list'),
    path('appointment/', views.appointment, name='appointment'),
    path('register/', views.register, name='register'),
]
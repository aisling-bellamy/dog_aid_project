from django.urls import path
from dog_aid import views

app_name = 'dog_aid'

urlpatterns = [
    path('', views.first, name='first'),
    path('index/', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('training/', views.training, name='training'),
    path('vet_register/', views.registerVet, name='vet_register'),
    path('register_dog/', views.register_dog, name='register_dog'),
    path('register_event/', views.registerDogEvent, name='register_event'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('dog_profile/<name>/', views.DogProfileView.as_view(), name='dog_profile'),
    path('vet_profile/<name>/', views.VetProfileView.as_view(), name='vet_profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('dog_profile_list/', views.ListDogProfiles.as_view(), name='dog_profile_list'),
    path('vet_list/', views.ListVetProfiles.as_view(), name='vet_list'),
    path('register/', views.register, name='register'),
    path('suggest/', views.illness_suggest, name='illness_suggest'),
    path('emergency_suggest/', views.emergency_suggest, name='emergency_suggest'),
    path('illness_profile/<name>/', views.IllnessView.as_view(), name='illness_profile'),
    path('symptom_profile/<name>/', views.SymptomView.as_view(), name='symptom_profile'),
    path('illness_all/', views.ListIllnessView.as_view(), name='illness_all'),
    path('emergency/', views.ListSymptomsIllnessView.as_view(), name='emergency')
]
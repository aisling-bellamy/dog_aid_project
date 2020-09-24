from django.contrib import admin
from dog_aid.models import UserProfile, DogBreed, Dog, VetType, Vet, Symptom, Illness, DogEvent, DogEventType

admin.site.register(UserProfile)
admin.site.register(DogBreed)
admin.site.register(Dog)
admin.site.register(VetType)
admin.site.register(Vet)
admin.site.register(Symptom)
admin.site.register(Illness)
admin.site.register(DogEvent)
admin.site.register(DogEventType)

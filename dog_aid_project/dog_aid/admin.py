from django.contrib import admin
from dog_aid.models import UserProfile, DogOwner, DogProfile

admin.site.register(UserProfile)
admin.site.register(DogOwner)
admin.site.register(DogProfile)
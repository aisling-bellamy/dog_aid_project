from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class DogOwner(models.Model):
    owner_name = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    dog = models.CharField(max_length=128, blank=True)
    vet = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.owner_name

class DogProfile(models.Model):
    picture = models.ImageField(upload_to='dog_images', blank=True)
    owner = models.ForeignKey(DogOwner, on_delete=models.CASCADE, max_length=128, null=True)
    dog_name = models.CharField(max_length=128, blank=True)
    date_of_birth = models.DateField(max_length=128, null=True)
    breed_of_dog = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.dog_name

class DogBreed(models.Model):
    breed_name = models.ForeignKey(DogProfile, on_delete=models.CASCADE, max_length=128, null=True)
    breed_type = models.CharField(max_length=128, blank=True)

class VetProfile(models.Model):
    name_of_vet = models.CharField(max_length=128, blank=True)
    phone_number = models.IntegerField(default=0)
    street = models.CharField(max_length=128, blank=True)
    town = models.CharField(max_length=128, blank=True)
    county = models.CharField(max_length=128, blank=True)
    postcode = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name_of_vet

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


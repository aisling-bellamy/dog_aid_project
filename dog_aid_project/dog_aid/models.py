from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username

class DogBreed(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Dog(models.Model):
    dog_id = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='dog_images', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, max_length=128, null=True)
    name = models.CharField(max_length=128, blank=True)
    DOB = models.DateField(max_length=128, null=True)
    breed = models.ForeignKey(DogBreed, on_delete=models.CASCADE, max_length=128, blank=True)
    def __str__(self):
        return self.name

class DogEventType(models.Model):
    dog_event_id = models.IntegerField(default=0)
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class DogEvent(models.Model):
    name = models.CharField(max_length=128, blank=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    event_type = models.ForeignKey(DogEventType, on_delete=models.CASCADE)
    date = models.DateField(max_length=128, null=True)
    notes = models.TextField(max_length=1000, blank=True)
    def __str__(self):
        return self.name

class VetType(models.Model):
    vet_type_id = models.IntegerField(default=0)
    name = models.CharField(max_length=128, blank=True)
    def __str__(self):
        return self.name

class Vet(models.Model):
    name = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=500)
    address = models.CharField(max_length=500, blank=True)
    type = models.ForeignKey(VetType, on_delete=models.CASCADE, null=True)
    dog_owner = models.ForeignKey(User, on_delete=models.CASCADE, max_length=128, null=True)
    def __str__(self):
        return self.name

class Symptom(models.Model):
    symptom_id = models.IntegerField(default=0)
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1000, blank=True)
    picture = models.ImageField(upload_to='symptom_images', blank=True)
    def __str__(self):
        return self.name

class Illness(models.Model):
    illness_id = models.IntegerField(default=0)
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    picture = models.ImageField(upload_to='illness_images', blank=True)
    related_symptom = models.ManyToManyField(Symptom)
    treatment = models.TextField(max_length=1000, blank=True)
    call_vet = models.TextField(max_length=300, blank=True)
    def __str__(self):
        return self.name

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

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dog_aid_project.settings')
import django
django.setup()
from dog_aid.models import UserProfile

def populate():
    users = [
        {'user': 'Fiona',
         'picture': ''}]

    cats = {'User profiles': {'User Profiles': users}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['users']:
            add_page(c, p['user'], p['picture'])

    for c in UserProfile.objects.all():
            print(f'- {c}: {p}')

def add_user(cat, user, picture):
    p = Page.objects.get_or_create(category=cat, user=user)[0]
    p.save()
    return p

def add_cat(user, views=0, likes=0):
    c = UserProfile.objects.get_or_create(user=user)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
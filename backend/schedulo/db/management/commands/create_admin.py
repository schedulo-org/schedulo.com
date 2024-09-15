from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Create a superuser.'

    def handle(self, *args, **options):
        """
        Creates a superuser if one does not already exist.

        The username, email, and password are set from the environment variables
        DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, and DJANGO_SUPERUSER_PASSWORD
        respectively.
        """
        User = get_user_model()
        if not User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists():
            User.objects.create_superuser(
                username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
                email=os.getenv('DJANGO_SUPERUSER_EMAIL'),
                password=os.getenv('DJANGO_SUPERUSER_PASSWORD')
            )
            print('Superuser created.')
        else:
            print('Superuser already exists.')

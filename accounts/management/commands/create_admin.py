from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password=os.getenv("ADMIN_PASSWORD", "admin"),
            )
            self.stdout.write("superuser created")
        else:
            self.stdout.write("superuser already exists")
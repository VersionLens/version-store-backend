import os
import shutil
import random

from django.core.management.base import BaseCommand
from django.conf import settings

from main.models import Product, Basket


class Command(BaseCommand):
    help = "Creates initial Product models"

    def handle(self, *args, **options):
        imgs = []

        # Copy images from settings.BASE_DIR/main/static/img to settings.MEDIA_ROOT
        for img in os.listdir(os.path.join(settings.BASE_DIR, "main/static/img")):
            shutil.copy(
                os.path.join(settings.BASE_DIR, "main/static/img", img),
                os.path.join(settings.MEDIA_ROOT, "products", img),
            )
            imgs.append(img)

        # Create initial Product models from images, using ImageField
        for img in imgs:
            try:
                Product.objects.create(
                    name=img.split(".")[0],
                    price=random.randint(10, 20),
                    image=f"products/{img}",
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed to create initial Product model: {e}")
                )

        # Create initial global Basket
        Basket.get()

        self.stdout.write(
            self.style.SUCCESS("Successfully created initial Product models")
        )

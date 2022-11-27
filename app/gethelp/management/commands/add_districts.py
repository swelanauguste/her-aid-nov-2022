from django.core.management.base import BaseCommand

from ...models import District


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/txt/districts.txt") as file:
            for row in file:
                district = row.replace("\n", "")
                District.objects.get_or_create(
                    district=district,
                )
                self.stdout.write(self.style.SUCCESS(f"{district} added"))
                

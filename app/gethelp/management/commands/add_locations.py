import csv

from django.core.management.base import BaseCommand

from ...models import Location, District


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open(f"static/csv/locations.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                location = row[1].replace("\n", "")
                district = District.objects.get(pk=int(row[0]))
                Location.objects.get_or_create(
                    location=location,
                    district=district,
                )
                self.stdout.write(self.style.SUCCESS(f"{location} added"))

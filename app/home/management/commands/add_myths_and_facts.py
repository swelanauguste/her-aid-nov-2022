import csv

from django.core.management.base import BaseCommand

from ...models import MythAndFact

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/csv/myths-and-facts.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                title = row[0].lower().replace("\n", "")
                details = row[1].lower().replace("\n", "")
                MythAndFact.objects.get_or_create(
                    title=title,
                    details=details,
                )
                self.stdout.write(self.style.SUCCESS(f"{title} added"))
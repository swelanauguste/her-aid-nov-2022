import csv

from django.core.management.base import BaseCommand

from ...models import FAQ

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/csv/faqs.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                title = row[0].lower().replace("\n", "")
                details = row[1].lower().replace("\n", "")
                FAQ.objects.get_or_create(
                    title=title,
                    details=details,
                )
                self.stdout.write(self.style.SUCCESS(f"{title} added"))
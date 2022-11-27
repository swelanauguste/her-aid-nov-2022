import csv

from django.core.management.base import BaseCommand

from ...models import FAQ

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/csv/faqs.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                question = row[0].replace("\n", "")
                details = row[1].replace("\n", "")
                FAQ.objects.get_or_create(
                    question=question,
                    details=details,
                )
                self.stdout.write(self.style.SUCCESS(f"{question} added"))
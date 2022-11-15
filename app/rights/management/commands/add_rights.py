import csv

from django.core.management.base import BaseCommand

from ...models import Right

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/csv/rights.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                title = row[0].lower().replace("\n", "")
                sub_title = row[1].lower().replace("\n", "")
                details = row[2].lower().replace("\n", "")
                Right.objects.get_or_create(
                    title=title,
                    sub_title=sub_title,
                    details=details,
                )
                self.stdout.write(self.style.SUCCESS(f"{title} added"))
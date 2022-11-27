from django.core.management.base import BaseCommand

from ...models import Screening

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open(f"static/txt/screening-questions.txt") as file:
            for row in file:
                question = row.replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{question} added"))
                Screening.objects.get_or_create(
                    question=question,
                )
        self.stdout.write(self.style.SUCCESS("list of questions added"))

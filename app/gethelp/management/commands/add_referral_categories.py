from django.core.management.base import BaseCommand

from ...models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/txt/referral_categories.txt") as file:
            for row in file:
                category = row.replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{category} added"))
                Category.objects.get_or_create(
                    category=category,
                )
        self.stdout.write(self.style.SUCCESS("list of categories added"))

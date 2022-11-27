import csv

from django.core.management.base import BaseCommand

from ...models import Referral, Category, Location

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/csv/LC_GBV_Referrals.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                name = row[7].replace("\n", "")
                remote_services = row[2].replace("\n", "")
                location = Location.objects.get(pk=int(row[1]))
                hotline = row[3].replace("\n", "")
                tel = row[4].replace("\n", "")
                tel1 = row[5].replace("\n", "")
                tel2 = row[6].replace("\n", "")
                organization = row[8].replace("\n", "")
                funded_by = row[9].replace("\n", "")
                sector = row[10].replace("\n", "")
                service = row[11].replace("\n", "")
                open_hours = row[12].replace("\n", "")
                for_women = int(row[13].replace("\n", ""))
                for_girls = int(row[14])
                for_boys = int(row[15])
                for_men = int(row[16])
                for_seniors = int(row[17])
                for_homeless = int(row[18])
                for_disabled = int(row[19])
                for_lgbt = int(row[20])
                for_refugees = int(row[21])
                category = Category.objects.get(pk=int(row[22]))
                Referral.objects.get_or_create(
                    name=name,
                    remote_services=remote_services,
                    location=location,
                    hotline=hotline,
                    tel=tel,
                    tel1=tel1,
                    tel2=tel2,
                    organization=organization,
                    funded_by=funded_by,
                    sector=sector,
                    service=service,
                    open_hours=open_hours,
                    for_women=for_women,
                    for_girls=for_girls,
                    for_boys=for_boys,
                    for_men=for_men,
                    for_seniors=for_seniors,
                    for_homeless=for_homeless,
                    for_disabled=for_disabled,
                    for_lgbt=for_lgbt,
                    for_refugees=for_refugees,
                    category=category,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                
            
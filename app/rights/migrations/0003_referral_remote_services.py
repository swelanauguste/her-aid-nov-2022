# Generated by Django 4.1.3 on 2022-11-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rights", "0002_referral"),
    ]

    operations = [
        migrations.AddField(
            model_name="referral",
            name="remote_services",
            field=models.BooleanField(default=1),
        ),
    ]
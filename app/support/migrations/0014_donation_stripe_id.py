# Generated by Django 4.1.3 on 2023-03-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0013_rename_donate_donation"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="stripe_id",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

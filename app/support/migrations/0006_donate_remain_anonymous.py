# Generated by Django 4.1.3 on 2023-03-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0005_donate_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="donate",
            name="remain_anonymous",
            field=models.BooleanField(default=True),
        ),
    ]

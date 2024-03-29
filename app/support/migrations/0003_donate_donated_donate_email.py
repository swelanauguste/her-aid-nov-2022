# Generated by Django 4.1.3 on 2023-03-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0002_donate_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="donate",
            name="donated",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="donate",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]

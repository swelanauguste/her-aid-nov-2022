# Generated by Django 4.1.3 on 2023-03-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="donate",
            name="note",
            field=models.TextField(blank=True),
        ),
    ]
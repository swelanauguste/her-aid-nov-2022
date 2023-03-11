# Generated by Django 4.1.3 on 2023-03-11 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0003_donate_donated_donate_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="donate",
            name="amt",
        ),
        migrations.AddField(
            model_name="donate",
            name="amount",
            field=models.DecimalField(
                decimal_places=2,
                default=5.0,
                max_digits=9,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
        ),
    ]

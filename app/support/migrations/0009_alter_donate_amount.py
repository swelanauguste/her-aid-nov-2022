# Generated by Django 4.1.3 on 2023-03-12 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0008_alter_donate_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donate",
            name="amount",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=9,
                validators=[django.core.validators.MinValueValidator(0.01)],
            ),
        ),
    ]
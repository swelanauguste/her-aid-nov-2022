# Generated by Django 4.1.3 on 2022-11-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gethelp", "0012_alter_location_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="location",
            field=models.CharField(max_length=100),
        ),
    ]
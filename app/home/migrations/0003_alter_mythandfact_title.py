# Generated by Django 4.1.3 on 2022-11-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_title_faq_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mythandfact",
            name="title",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

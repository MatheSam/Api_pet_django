# Generated by Django 4.1.1 on 2022-10-04 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="animal",
        ),
    ]

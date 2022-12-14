# Generated by Django 4.1.1 on 2022-10-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0002_remove_trait_animal"),
        ("animals", "0006_animal_animal"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="animal",
            name="animal",
        ),
        migrations.AddField(
            model_name="animal",
            name="trait",
            field=models.ManyToManyField(related_name="animals", to="traits.trait"),
        ),
    ]

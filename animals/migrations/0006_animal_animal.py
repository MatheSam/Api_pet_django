# Generated by Django 4.1.1 on 2022-10-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("animals", "0005_alter_animal_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="animal",
            field=models.ManyToManyField(related_name="traits", to="animals.animal"),
        ),
    ]

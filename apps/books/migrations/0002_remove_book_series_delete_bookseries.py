# Generated by Django 5.0.7 on 2024-07-14 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="series",
        ),
        migrations.DeleteModel(
            name="BookSeries",
        ),
    ]

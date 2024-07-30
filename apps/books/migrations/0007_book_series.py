# Generated by Django 5.0.7 on 2024-07-14 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_alter_book_entered_at"),
        ("series", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="series",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="books",
                to="series.series",
            ),
        ),
    ]

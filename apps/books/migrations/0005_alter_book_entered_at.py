# Generated by Django 5.0.7 on 2024-07-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0004_bookphoto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="entered_at",
            field=models.DateTimeField(null=True),
        ),
    ]
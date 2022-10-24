# Generated by Django 4.1.1 on 2022-10-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=50)),
                ("email", models.TextField(max_length=100)),
                ("address", models.TextField()),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
    ]

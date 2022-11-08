# Generated by Django 4.1.1 on 2022-09-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=20, unique=True)),
                ("avatar_url", models.CharField(blank=True, max_length=200)),
                ("avatar_name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("message_author", models.CharField(max_length=20)),
                ("message_room", models.CharField(max_length=20)),
                ("message_text", models.TextField(blank=True)),
                ("message_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("room_name", models.CharField(max_length=20, unique=True)),
                ("room_date", models.DateTimeField(auto_now_add=True)),
                ("room_author", models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]

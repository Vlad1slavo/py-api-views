# Generated by Django 4.1 on 2024-01-02 09:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0002_actor_cinemahall_genre_alter_movie_title_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cinemahall",
            old_name="sets_in_row",
            new_name="seats_in_row",
        ),
    ]
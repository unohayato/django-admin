# Generated by Django 4.1.6 on 2023-02-09 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book", options={"verbose_name": "本", "verbose_name_plural": "本たち"},
        ),
    ]
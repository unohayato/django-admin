# Generated by Django 4.1.6 on 2023-02-12 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_book_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="user",),
        migrations.AddField(
            model_name="book",
            name="user_id",
            field=models.IntegerField(default=1, editable=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-27 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210127_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_genres',
            old_name='author',
            new_name='book',
        ),
    ]
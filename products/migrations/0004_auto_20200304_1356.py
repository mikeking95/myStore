# Generated by Django 2.2.10 on 2020-03-04 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]

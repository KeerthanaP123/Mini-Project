# Generated by Django 3.1.2 on 2023-02-24 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20230224_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bk_pdf',
        ),
    ]

# Generated by Django 3.1.2 on 2023-02-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_tbl_elibrary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bk_pdf',
            field=models.FileField(blank=True, default=0, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='tbl_elibrary',
        ),
    ]

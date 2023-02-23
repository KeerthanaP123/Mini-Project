# Generated by Django 3.1.2 on 2023-02-21 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20221123_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Returnbook',
            fields=[
                ('return_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_return', models.DateTimeField(auto_now_add=True)),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tbl_bookissue')),
            ],
        ),
    ]

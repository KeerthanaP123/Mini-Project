# Generated by Django 3.1.2 on 2022-11-22 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20221119_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_BookIssue',
            fields=[
                ('issue_id', models.AutoField(primary_key=True, serialize=False)),
                ('reqid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bookrequest')),
            ],
        ),
    ]

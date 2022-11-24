# Generated by Django 3.1.2 on 2022-11-18 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('contact', models.BigIntegerField(default=0)),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=50)),
                ('pincode', models.BigIntegerField(default='0')),
                ('dob', models.DateField(default=0)),
                ('roles', models.CharField(choices=[('is_customer', 'is_customer'), ('is_librarian', 'is_librarian'), ('None', 'None')], default='', max_length=100)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('None', 'None')], default='Pending', max_length=40)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_librarian', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bk_id', models.AutoField(primary_key=True, serialize=False)),
                ('bk_title', models.CharField(max_length=100)),
                ('bk_author', models.CharField(max_length=100)),
                ('bk_publisher', models.CharField(max_length=200)),
                ('bk_pubyear', models.BigIntegerField()),
                ('bk_pubagency', models.CharField(max_length=200)),
                ('bk_edition', models.BigIntegerField()),
                ('bk_isbn', models.BigIntegerField()),
                ('bk_noofpages', models.BigIntegerField()),
                ('bk_price', models.BigIntegerField()),
                ('bk_stno', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('cat_name',),
            },
        ),
        migrations.CreateModel(
            name='Profile_update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestdate', models.DateTimeField(auto_now_add=True)),
                ('requestedstatus', models.CharField(max_length=30)),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='bk_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]

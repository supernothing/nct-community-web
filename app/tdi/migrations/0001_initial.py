# Generated by Django 2.1.4 on 2018-12-26 17:16

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('invitecode', models.CharField(max_length=30)),
                ('maxuses', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Access codes',
            },
        ),
        migrations.CreateModel(
            name='WhitepaperAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('invitecode', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Whitepaper access',
            },
        ),
        migrations.CreateModel(
            name='WhitepaperAccessRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('comments', models.TextField(max_length=5000)),
                ('email', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=30)),
                ('processed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

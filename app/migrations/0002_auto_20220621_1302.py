# Generated by Django 2.2.4 on 2022-06-21 07:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aditor_Detail',
            new_name='Foreign_Server',
        ),
        migrations.RenameModel(
            old_name='Cloud',
            new_name='Mother_Server',
        ),
        migrations.AddField(
            model_name='upload_file',
            name='foreign_private_key',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Secret Key'),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='foreign_public_key',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Foreign Public Key'),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='foreign_status',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Foreign Status'),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='level_server',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='upload_file',
            name='upoaded_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 21, 7, 32, 23, 874067, tzinfo=utc), verbose_name='Uploaded Date'),
        ),
    ]

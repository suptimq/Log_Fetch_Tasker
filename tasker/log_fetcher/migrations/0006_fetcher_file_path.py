# Generated by Django 2.0.8 on 2018-12-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_fetcher', '0005_remove_fetcher_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='fetcher',
            name='file_path',
            field=models.CharField(blank=True, help_text="You don't have to fill it", max_length=100, null=True, verbose_name='log path'),
        ),
    ]

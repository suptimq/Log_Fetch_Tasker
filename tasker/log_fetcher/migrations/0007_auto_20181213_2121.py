# Generated by Django 2.0.8 on 2018-12-13 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('log_fetcher', '0006_fetcher_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fetcher',
            name='file_path',
            field=models.CharField(blank=True, default=django.utils.timezone.now, help_text="You don't have to fill it", max_length=100, verbose_name='log path'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.6 on 2018-08-03 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haikuapp', '0006_auto_20180803_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='html_file_name',
        ),
        migrations.AddField(
            model_name='template',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_imageblog_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='seconde/'),
        ),
    ]

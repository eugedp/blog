# Generated by Django 4.1.5 on 2023-03-02 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_blogimage_image_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
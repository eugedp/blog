# Generated by Django 4.1.5 on 2023-01-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_blogpost_image_imageblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageblog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
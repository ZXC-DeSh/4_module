# Generated by Django 4.2.3 on 2023-08-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0003_advertisement_image_advertisement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='advertisements/', verbose_name='Изображение'),
        ),
    ]

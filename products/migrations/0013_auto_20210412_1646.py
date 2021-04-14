# Generated by Django 3.2 on 2021-04-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210404_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digital_media',
            name='name',
            field=models.CharField(choices=[('icon_sets', 'Icon Sets'), ('brand_logos', 'Brand Logos'), ('web_banners', 'Web Banners')], default='Digital_Media', max_length=20),
        ),
        migrations.AlterField(
            model_name='digital_media',
            name='size',
            field=models.CharField(choices=[('1616', '16 x 16 pixels'), ('3232', '32 x 32 pixels'), ('6464', '64 x 64 pixels'), ('128128', '128 x 128 pixels'), ('256256', '256 x 256 pixels')], default='Size', max_length=20),
        ),
    ]
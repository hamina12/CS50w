# Generated by Django 4.1.6 on 2023-02-12 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_image_remove_aunction_pic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aunction',
            new_name='Auction',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='aunction',
            new_name='auction',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='aunction',
            new_name='auction',
        ),
    ]
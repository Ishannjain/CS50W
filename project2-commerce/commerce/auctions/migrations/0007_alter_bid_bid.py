# Generated by Django 5.1.4 on 2025-02-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_bid_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.IntegerField(default=0),
        ),
    ]

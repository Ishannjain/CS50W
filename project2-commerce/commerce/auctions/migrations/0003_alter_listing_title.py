# Generated by Django 5.1.4 on 2025-02-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_rename_categories_listing_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=90),
        ),
    ]

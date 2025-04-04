# Generated by Django 5.1.4 on 2025-02-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='categories',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='decsription',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-04-12 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_item_category_item_uploaded_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'ordering': ('name',), 'verbose_name_plural': 'Faculties'},
        ),
    ]
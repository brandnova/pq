# Generated by Django 5.0.1 on 2024-01-23 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_item_decsription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='decsription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='item',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='docs.department'),
        ),
        migrations.AlterField(
            model_name='item',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='docs.faculty'),
        ),
        migrations.AlterField(
            model_name='item',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='docs.level'),
        ),
        migrations.AlterField(
            model_name='item',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='docs.semester'),
        ),
    ]

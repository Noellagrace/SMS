# Generated by Django 5.0.4 on 2024-05-23 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_utilisateur', '0007_delete_matiere'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestion_utilisateur.classe'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-16 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='email',
            new_name='email_mere',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='nom',
            new_name='nom_mere',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='prenom',
            new_name='nom_pere',
        ),
        migrations.RenameField(
            model_name='parent',
            old_name='telephone',
            new_name='telephone_mere',
        ),
        migrations.AddField(
            model_name='classe',
            name='montant',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='email_pere',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='prenom_mere',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='prenom_pere',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='telephone_pere',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personnel_ad',
            name='poste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='gestion_utilisateur.poste'),
        ),
    ]
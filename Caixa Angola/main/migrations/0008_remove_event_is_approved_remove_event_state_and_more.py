# Generated by Django 4.0.5 on 2022-06-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_event_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='event',
            name='state',
        ),
        migrations.AddField(
            model_name='oportunidade',
            name='is_approved',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oportunidade',
            name='state',
            field=models.CharField(choices=[('Em espera', 'Em espera'), ('Em progresso', 'Em progresso'), ('Finalizado', 'Finalizado')], default=1, max_length=120),
            preserve_default=False,
        ),
    ]
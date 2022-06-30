from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_oportunidade_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidade',
            name='recursos',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default=1, max_length=120),
            preserve_default=False,
        ),
    ]

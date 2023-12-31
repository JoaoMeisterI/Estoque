# Generated by Django 4.2.2 on 2023-08-09 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_materias_local_alter_destino_local_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materias',
            name='local',
        ),
        migrations.AlterField(
            model_name='destino',
            name='local',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destino',
            name='motivo',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='destino',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.materias'),
        ),
    ]

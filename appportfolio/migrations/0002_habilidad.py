# Generated by Django 4.1.5 on 2024-10-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appportfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('habilidad', models.CharField(blank=True, max_length=30, null=True, verbose_name='Habilidad')),
                ('nivel', models.CharField(blank=True, max_length=30, null=True, verbose_name='nivel')),
                ('Comentario', models.CharField(blank=True, max_length=30, null=True, verbose_name='Comentario')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['habilidad'],
            },
        ),
    ]

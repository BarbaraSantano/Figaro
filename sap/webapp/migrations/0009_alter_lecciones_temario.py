# Generated by Django 4.0.5 on 2022-07-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_calificaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecciones',
            name='temario',
            field=models.FileField(null=True, upload_to='temario/'),
        ),
    ]
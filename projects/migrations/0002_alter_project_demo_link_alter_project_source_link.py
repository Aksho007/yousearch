# Generated by Django 4.1.5 on 2023-01-30 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

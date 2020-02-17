# Generated by Django 3.0.3 on 2020-02-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200217_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='chartUrl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='idcMdgId',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sector',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]

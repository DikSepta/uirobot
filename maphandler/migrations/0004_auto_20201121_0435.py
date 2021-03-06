# Generated by Django 3.1.3 on 2020-11-21 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maphandler', '0003_auto_20201120_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robotmap',
            name='scale_x',
            field=models.PositiveIntegerField(default=0, help_text='map horizontal scale in 1 pixel : xx meter'),
        ),
        migrations.AlterField(
            model_name='robotmap',
            name='scale_y',
            field=models.PositiveIntegerField(default=0, help_text='map vertical scale in 1 pixel : xx meter'),
        ),
        migrations.AlterField(
            model_name='robotmap',
            name='size_x',
            field=models.FloatField(blank=True, default=0, help_text='map horizontal size in pixel'),
        ),
        migrations.AlterField(
            model_name='robotmap',
            name='size_y',
            field=models.FloatField(blank=True, default=0, help_text='map vertical size in pixel'),
        ),
    ]

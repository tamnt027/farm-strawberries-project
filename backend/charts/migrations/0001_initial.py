# Generated by Django 4.1.2 on 2022-10-27 07:34

import colorfield.fields
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChartGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoraDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('device_id', models.CharField(help_text='Dev UID', max_length=50, unique=True)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoraMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeriesDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('mode', models.CharField(choices=[('lines', 'Lines')], default='lines', help_text='Chart mode', max_length=16)),
                ('chart_type', models.CharField(choices=[('scatter', 'Scatter')], default='scatter', help_text='Chart type', max_length=16)),
                ('color', colorfield.fields.ColorField(default='#0000FF', image_field=None, max_length=18, samples=None)),
                ('yaxis', models.CharField(choices=[('y1', 'Yaxis1'), ('y2', 'Yaxis2')], default='y1', help_text='Y axis 1 for left, Y axis 2 for right', max_length=10)),
                ('device', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='series', to='charts.loradevice')),
                ('measurement', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='series', to='charts.lorameasurement')),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=256, null=True)),
                ('display_priority', models.PositiveSmallIntegerField(default=0, help_text='Smaller value has higher priority to appear')),
                ('title_size', models.IntegerField(default=20, help_text='Title font size', validators=[django.core.validators.MinValueValidator(8)])),
                ('title_color', colorfield.fields.ColorField(default='#000000', help_text='Title color', image_field=None, max_length=18, samples=None)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('active', models.BooleanField(default=True, help_text='Uncheck to prevent displaying')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='charts', to='charts.chartgroup')),
                ('series_displays', models.ManyToManyField(blank=True, related_name='in_charts', to='charts.seriesdisplay')),
            ],
        ),
    ]
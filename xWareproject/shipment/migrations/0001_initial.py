# Generated by Django 4.2.3 on 2023-09-19 13:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trip', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(choices=[('United States of America', 'USA'), ('Canada', 'CAN'), ('United Kingdom', 'UK'), ('Australia', 'AUS'), ('France', 'FRA'), ('Germany', 'GER'), ('Japan', 'JPN'), ('India', 'IND'), ('Brazil', 'BRA'), ('South Africa', 'SAF'), ('Egypt', 'EGY'), ('Sudan', 'SDN'), ('Saudi Arabia', 'SAU'), ('Syria', 'SYR'), ('Mexico', 'MEX'), ('Italy', 'ITA'), ('Spain', 'ESP'), ('China', 'CHN'), ('Russia', 'RUS'), ('Argentina', 'ARG')], max_length=50)),
                ('to_location', models.CharField(choices=[('United States of America', 'USA'), ('Canada', 'CAN'), ('United Kingdom', 'UK'), ('Australia', 'AUS'), ('France', 'FRA'), ('Germany', 'GER'), ('Japan', 'JPN'), ('India', 'IND'), ('Brazil', 'BRA'), ('South Africa', 'SAF'), ('Egypt', 'EGY'), ('Sudan', 'SDN'), ('Saudi Arabia', 'SAU'), ('Syria', 'SYR'), ('Mexico', 'MEX'), ('Italy', 'ITA'), ('Spain', 'ESP'), ('China', 'CHN'), ('Russia', 'RUS'), ('Argentina', 'ARG')], max_length=50)),
                ('name_shipment', models.CharField(max_length=20)),
                ('before_date', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
                ('shipment_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='enter valid weight.'), django.core.validators.MaxValueValidator(limit_value=100.0, message='Item weight cannot exceed 100.0.')])),
                ('trip_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trip.trip')),
                ('user_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_link', models.URLField()),
                ('item_name', models.CharField(max_length=100)),
                ('item_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='enter valid weight.'), django.core.validators.MaxValueValidator(limit_value=100.0, message='Item weight cannot exceed 100.0.')])),
                ('single_item_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rate', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('shipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.shipment')),
            ],
        ),
    ]

# Generated by Django 2.2.12 on 2023-09-17 15:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(choices=[('usa', 'United Status America'), ('ca', 'canada'), ('kwt', 'kewit'), ('egy', 'egypt'), ('ksa', 'saudi')], max_length=20)),
                ('to_location', models.CharField(choices=[('usa', 'United Status America'), ('ca', 'canada'), ('kwt', 'kewit'), ('egy', 'egypt'), ('ksa', 'saudi')], max_length=20)),
                ('name_shipment', models.CharField(max_length=20)),
                ('before_date', models.DateField()),
                ('quantity', models.IntegerField(default=0)),
                ('trip_object', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='trip.Trip')),
                ('user_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_link', models.URLField()),
                ('item_name', models.CharField(max_length=100)),
                ('item_weight', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0.0, message='enter valid weight.'), django.core.validators.MaxValueValidator(limit_value=100.0, message='Item weight cannot exceed 100.0.')])),
                ('single_item_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('shipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.Shipment')),
            ],
        ),
    ]

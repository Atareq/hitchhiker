# Generated by Django 4.2.3 on 2023-09-14 20:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=1000)),
                ('location_from', models.CharField(choices=[('usa', 'United Status America'), ('ca', 'canada'), ('kwt', 'kewit'), ('egy', 'egypt'), ('ksa', 'saudi')], max_length=10)),
                ('location_to', models.CharField(choices=[('usa', 'United Status America'), ('ca', 'canada'), ('kwt', 'kewit'), ('egy', 'egypt'), ('ksa', 'saudi')], max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('weight_available', models.FloatField()),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('user_t', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

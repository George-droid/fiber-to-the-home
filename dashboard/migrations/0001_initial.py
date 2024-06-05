# Generated by Django 3.2.13 on 2022-07-27 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressLine1', models.CharField(blank=True, max_length=100, null=True)),
                ('addressLine2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=100, null=True)),
                ('profileImage', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=90, scale=None, size=[100, 100], upload_to='profile_image')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

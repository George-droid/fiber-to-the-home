# Generated by Django 3.2.13 on 2022-12-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_faqs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coverage_name', models.CharField(max_length=100)),
                ('strength', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0, max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2023-03-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookparking', '0002_alter_reserveuser_is_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=25)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('long', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]

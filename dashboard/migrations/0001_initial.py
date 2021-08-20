# Generated by Django 3.2.4 on 2021-08-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=30)),
                ('AmcType', models.CharField(max_length=30)),
                ('AmcWarrenty', models.IntegerField()),
                ('MaxFeeServices', models.IntegerField()),
                ('StartDate', models.DateField(max_length=30)),
                ('EndDate', models.DateField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]

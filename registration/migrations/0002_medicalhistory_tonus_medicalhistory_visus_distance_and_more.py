# Generated by Django 4.0.2 on 2024-04-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalhistory',
            name='tonus',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='visus_distance',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='visus_near',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
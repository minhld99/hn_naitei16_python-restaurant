# Generated by Django 3.1.2 on 2021-09-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210826_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='rzp_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='bill',
            name='rzp_payment_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='bill',
            name='rzp_signature',
            field=models.CharField(default='', max_length=255),
        ),
    ]

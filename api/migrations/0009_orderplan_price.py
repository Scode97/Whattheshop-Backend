# Generated by Django 2.1 on 2018-09-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180910_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplan',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

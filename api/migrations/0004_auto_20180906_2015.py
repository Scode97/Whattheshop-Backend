# Generated by Django 2.1 on 2018-09-06 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180906_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plans',
            old_name='totalPrice',
            new_name='Price',
        ),
        migrations.AddField(
            model_name='plans',
            name='Description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]

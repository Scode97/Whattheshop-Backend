# Generated by Django 2.1 on 2018-09-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180904_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofmeals',
            name='Ready_In',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='listofmeals',
            name='cook',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='listofmeals',
            name='prep',
            field=models.CharField(default='', max_length=250),
        ),
    ]
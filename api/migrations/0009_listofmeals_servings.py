# Generated by Django 2.1 on 2018-09-04 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_listofmeals_nutrition_facts'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofmeals',
            name='servings',
            field=models.CharField(default='', max_length=250),
        ),
    ]

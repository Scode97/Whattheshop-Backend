# Generated by Django 2.1 on 2018-09-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_productlist_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealTypeList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='ProductList',
            new_name='PlanList',
        ),
    ]

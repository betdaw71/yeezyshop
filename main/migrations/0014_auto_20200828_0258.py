# Generated by Django 2.1.5 on 2020-08-27 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='yeezysome'),
        ),
    ]
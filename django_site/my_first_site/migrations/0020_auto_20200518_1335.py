# Generated by Django 2.2.3 on 2020-05-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0019_auto_20200518_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='p_category',
            field=models.IntegerField(choices=[('notebook', 'note'), ('monitor', 'mon'), ('access', 'accessories')], null=True, verbose_name='Категория'),
        ),
    ]

# Generated by Django 2.2.3 on 2020-05-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0021_auto_20200518_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='p_category',
            field=models.CharField(blank=True, choices=[('notebook', 1), ('monitor', 2), ('access', 3)], max_length=40, null=True, verbose_name='Категория'),
        ),
    ]

# Generated by Django 2.2.3 on 2020-05-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0013_auto_20200517_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='p_category',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Категория'),
        ),
    ]

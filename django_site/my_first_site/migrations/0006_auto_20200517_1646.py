# Generated by Django 2.2.3 on 2020-05-17 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_site', '0005_product_category_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='product_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_first_site.Product'),
        ),
    ]
from django.db import models
from django.urls import reverse


# Create your models here.

MANUFACTURER_CHOICES = (
    ('china', 'China'),
    ('japan', 'Japan'),
    ('taiwan', 'Taiwan'),
    ('korea', 'Korea'),
    ('usa', 'Usa'),
)


class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Производитель', max_length=50,
                            blank=True, null=True)
    country = models.CharField(choices=MANUFACTURER_CHOICES, verbose_name='Страна', max_length=50,
                               blank=True, null=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return (str(self.name))

    def note_manufacturer(self):
        return reverse('manufacturer_detail', args=[str(self.pk)])


class Product(models.Model):
    NOTEBOOK = 'notebook'
    MONITOR = 'monitor'
    CATEGORY_CHOICES = (
        (NOTEBOOK, 'notebook'),
        (MONITOR, 'monitor'),
    )
    brand = models.ForeignKey(
        Manufacturer, 
        verbose_name='Производитель',
        related_name='product_list',
        max_length=20,
        on_delete=models.CASCADE, null=True)
    name = models.CharField(
        verbose_name='Модель', 
        max_length=50,
        blank=True, 
        null=True, 
        unique=True)
    price = models.DecimalField(
        verbose_name='Цена', 
        max_digits=10,
        decimal_places=2, 
        null=True)
    category = models.CharField(
        verbose_name='Категория', 
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='')
    image = models.ImageField(blank=True, null=True)
    descrip = models.ForeignKey(
        'Description', 
        verbose_name='Характеристики товара', 
        blank=True, 
        max_length=20, 
        null=True, 
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.pk)])


class Description(models.Model):
    product_name = models.ForeignKey(Product,
                                     max_length=30,
                                     null=True,
                                     on_delete=models.CASCADE)
    processor = models.CharField(blank=True, max_length=50, null=True)
    memory = models.CharField(blank=True, max_length=20, null=True)
    hdd = models.CharField(blank=True, max_length=20, null=True)
    videocard = models.CharField(blank=True, max_length=20, null=True)
    screen = models.CharField(blank=True, max_length=50, null=True)
    os = models.CharField(blank=True, max_length=30, null=True)
    connector = models.CharField(blank=True, max_length=50, null=True)
    color = models.CharField(blank=True, max_length=20, null=True)
    diagonal = models.CharField(blank=True, max_length=20, null=True)
    resolution = models.CharField(blank=True, max_length=20, null=True)
    frequency = models.CharField(blank=True, max_length=20, null=True)

    class Meta:
        verbose_name = 'Характеристики'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.product_name.name

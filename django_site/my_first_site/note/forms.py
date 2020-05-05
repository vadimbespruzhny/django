from django.forms import ModelForm
from my_first_site.note.models import Product, Manufacturer


class NotebookForm(ModelForm):
    class Meta:
        model = Product
        fields = ('brand', 'name', 'price')


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'country')

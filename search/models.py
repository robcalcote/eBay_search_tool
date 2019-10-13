from django.db import models

# Create your models here.
class Search(models.Model):
    search_term = models.CharField(max_length=200)
    price_limit = models.DecimalField(max_digits=10, decimal_places=2)
    search_date = models.DateTimeField('date searched')
    def __str__(self):
        return self.search_term

class Item(models.Model):
    search = models.ForeignKey(Search, on_delete=models.PROTECT)
    item_name = models.CharField(max_length=200)
    amazon_identification = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.item_name
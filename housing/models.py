from django.db import models

# static data
AREA_OPTIONS = [
    ('SqFt', 'SqFt'),
]
HOME_TYPE_OPTIONS = [
    ('Single Family', 'SingleFamily')
]


class HouseData(models.Model):
    """
    Information about houses
    """
    area_unit = models.CharField(choices=AREA_OPTIONS, null=True, blank=True, max_length=50)
    bathrooms = models.FloatField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    home_size = models.IntegerField(null=True, blank=True)
    home_type = models.CharField(choices=HOME_TYPE_OPTIONS, null=True, blank=True, max_length=100)
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.IntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    property_size = models.IntegerField(null=True, blank=True)
    rent_price = models.IntegerField(null=True, blank=True)
    rentzestimate_amount = models.IntegerField(null=True, blank=True)
    rentzestimate_last_updated = models.DateField(null=True, blank=True)
    tax_value = models.IntegerField(null=True, blank=True)
    tax_year = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)
    zestimate_amount = models.IntegerField(null=True, blank=True)
    zestimate_last_updated = models.DateField(null=True, blank=True)
    zillow_id = models.IntegerField(unique=True, null=True, blank=True)  # assuming unique
    address = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, max_length=200)
    state = models.CharField(null=True, blank=True, max_length=50)
    zipcode = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return f'{self.zillow_id}-{self.city}'

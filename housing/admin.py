from django.contrib import admin
from .models import HouseData


class HouseDataAdmin(admin.ModelAdmin):
    list_display = (
        'zillow_id',
        'city',
        'price',
        'year_built',
    )

admin.site.register(HouseData, HouseDataAdmin)

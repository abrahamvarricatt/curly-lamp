import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from housing.models import HouseData


class DataConversion:

    def __init__(self, main_dict):
        self.main_dict = main_dict

    def convert_type(self, key, type_name):
        if not self.main_dict[key]:
            self.main_dict[key] = None
            return
        if type_name == 'float':
            self.main_dict[key] = float(self.main_dict[key])
        if type_name == 'int':
            self.main_dict[key] = int(float(self.main_dict[key]))  # to take care of decimal numbers
        if type_name == 'date':
            self.main_dict[key] = datetime.strptime(self.main_dict[key], '%m/%d/%Y')
        if type_name == 'price_int':
            temp = self.main_dict[key]
            try:
                first_letter = temp[0]
                last_letter = temp[-1]
                middle_part = temp[1:-1]
                if last_letter == 'K':
                    self.main_dict[key] = int(float(middle_part) * 1000)
                elif last_letter == 'M':
                    self.main_dict[key] = int(float(middle_part) * 1_000_000)
                else:
                    raise ValueError('unexpected format!!')
            except:
                raise ValueError('unable to parse price!!')


class Command(BaseCommand):
    help = 'Import houses from specified CSV file'

    def add_arguments(self, parser):
        parser.add_argument('input_csv', type=str)

    def handle(self, *args, **options):
        with open(options['input_csv']) as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                count += 1
                self.stdout.write(f'Processing entry = {count:03d}')
                # clean up the data
                temp = DataConversion(row)
                temp.convert_type('bathrooms', 'float')
                temp.convert_type('bedrooms', 'int')
                temp.convert_type('home_size', 'int')
                temp.convert_type('last_sold_date', 'date')
                temp.convert_type('last_sold_price', 'int')
                temp.convert_type('price', 'price_int')  # special conversion
                temp.convert_type('property_size', 'int')
                temp.convert_type('rent_price', 'int')
                temp.convert_type('rentzestimate_amount', 'int')
                temp.convert_type('rentzestimate_last_updated', 'date')
                temp.convert_type('tax_value', 'int')
                temp.convert_type('tax_year', 'int')
                temp.convert_type('year_built', 'int')
                temp.convert_type('zestimate_amount', 'int')
                temp.convert_type('zestimate_last_updated', 'date')
                temp.convert_type('zillow_id', 'int')

                data = HouseData.objects.update_or_create(zillow_id=row['zillow_id'], defaults=row)
                # data.save()
                # self.stdout.write(', '.join(row))

        self.stdout.write('File read over!!')

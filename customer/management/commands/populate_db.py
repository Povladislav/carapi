from django.core.management.base import BaseCommand

from scripts.populate_db import *


class Command(BaseCommand):
    help = "Populating our DBase"

    # def add_arguments(self, parser):
    #     ...

    def handle(self, *args, **options):
        populate_with_sql()
        populate_cars()
        populate_with_locations()
        populate_with_showrooms()
        populate_with_producers()
        populate_with_av_cars()

from django.core.management import BaseCommand
from PyfaseActionBase import PyfaseCore



class Command(BaseCommand):
    def handle(self, *args, **options):
        PyfaseCore.init_core(2323, 4646)

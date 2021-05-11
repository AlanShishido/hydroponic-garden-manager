from django.core.management import BaseCommand
from nutrient_state.actions import NutrientsDatabase


class Command(BaseCommand):
    def handle(self, *args, **options):
        NutrientsDatabase().execute()

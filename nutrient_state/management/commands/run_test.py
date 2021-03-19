from django.core.management import BaseCommand
from nutrient_state import testando


class Command(BaseCommand):
    def handle(self, *args, **options):
        testando.testando_funcao()
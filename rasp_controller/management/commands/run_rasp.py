from django.core.management import BaseCommand
from rasp_controller.actions import HydroponicSystem


class Command(BaseCommand):
    def handle(self, *args, **options):
        HydroponicSystem().execute(enable_tasks=True)

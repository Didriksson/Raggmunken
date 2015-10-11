from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Scans the menu"
    
    def handle(self, *args, **options):
        self.stdout.write("Scan menu command")
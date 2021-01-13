from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates room_types"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many room_types do you want to create"
        )

    def handle(self, *args, **options):
        room_types = [
            "Private Room",
            "Shared Room",
            "Hotel Room",
            "Twin Room",
        ]
        for r in room_types:
            RoomType.objects.create(name=r)
        self.stdout.write(self.style.SUCCESS(f"{len(room_types)} room_types created!"))

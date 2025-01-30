import random
from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seeds the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "property_id": "1",
                "host_id": "1",
                "name": "Luxury Villa",
                "description": "A beautiful villa with a private pool",
                "location": "Bali, Indonesia",
                "pricepernight": 200.00,
            },
            {
                "property_id": "2",
                "host_id": "2",
                "name": "Beach House",
                "description": "A cozy beach house with an ocean view",
                "location": "Malibu, California",
                "pricepernight": 150.00,
            },
            {
                "property_id": "3",
                "host_id": "3",
                "name": "Mountain Cabin",
                "description": "A rustic cabin in the mountains",
                "location": "Aspen, Colorado",
                "pricepernight": 100.00,
            },
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded sample listings data!"))

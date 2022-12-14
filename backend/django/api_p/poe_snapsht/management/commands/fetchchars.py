from django.core.management.base import BaseCommand
from poe_snapsht.models import Characters, SnapShots
from poe_snapsht.modules import parse
import asyncio


class Command(BaseCommand):
    help = 'Fetch tracked characters'

    def handle(self, *args, **options):

        char_list = Characters.objects.filter(tracked=True)

        new_list = []
        for item in char_list:
            new_list.append((item.account.account_name, item.character))

        chars = asyncio.run(parse.start_fetch(new_list))

        for char in chars:
            SnapShots.objects.create(character=Characters.objects.get(character=char['char'][1]),
                    character_info=char['info'],
                    items=char['items'],
                    passives=char['passives'],
                    xml_code=char['xml_code'],
                    stats=char['stats']
                )
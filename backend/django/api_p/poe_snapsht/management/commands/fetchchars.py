from django.core.management.base import BaseCommand
from poe_snapsht.models import Characters, SnapShots
from poe_snapsht.modules import parse
import asyncio


class Command(BaseCommand):
    help = 'Fetch tracked characters'

    def handle(self, *args, **options):

        char_list = Characters.objects.filter(tracked=True)

        # for char in char_list:
        #     char_info = parse.get_character_items(char.account.account_name, char.character)
        #     items = char_info.get('items')
        #     char_info = char_info.get('character')
        #     passives = parse.get_character_passives(char.account.account_name, char.character)

        #     SnapShots.objects.create(character_id=char, character_info=char_info, items=items, passives=passives)
        #     self.stdout.write(f'Character {char} fetched')
        new_list = []
        for item in char_list:
            new_list.append((item.account.account_name, item.character))

        chars = asyncio.run(parse.start_fetch(new_list))

        for char in chars:
            SnapShots.objects.create(character_id=Characters.objects.get(character=char[0][1]), character_info=char[1], items=char[2], passives=char[3])
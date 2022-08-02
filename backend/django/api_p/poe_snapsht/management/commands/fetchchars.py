from django.core.management.base import BaseCommand
from poe_snapsht.models import Characters, SnapShots
from poe_snapsht.modules import parse


class Command(BaseCommand):
    help = 'Fetch tracked characters'

    def handle(self, *args, **options):

        char_list = Characters.objects.filter(tracked=True)

        for char in char_list:
            char_info = parse.get_character_items(char.account.account_name, char.character)
            items = char_info.get('items')
            char_info = char_info.get('character')
            passives = parse.get_character_passives(char.account.account_name, char.character)

            SnapShots.objects.create(character_id=char, character_info=char_info, items=items, passives=passives)
            self.stdout.write(f'Character {char} fetched')

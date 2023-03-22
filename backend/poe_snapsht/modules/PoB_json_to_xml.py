import os
import glob
from django.conf import settings
from subprocess import Popen


def send_chars(chars: list):
    with open(os.path.join(settings.POB_SRC, 'CharList.lua'), 'w') as file:
        file.write(f'CharCount = {len(chars)}\n')
        file.write('CharList = {\n')
        for char in chars:
            file.write('\t{\n')
            for el in char:
                file.write('\t{ [====[')
                file.write(el)
                file.write(']====] },\n')
            file.write('\t},\n')
        file.write('}')

def get_pob_xmls(chars: list):
    """
    character must be List[items, passives]
    """
    send_chars(chars)

    # Check if ProcessJson.lua exists
    if not os.path.exists(os.path.join(settings.POB_SRC, 'ProcessJson.lua')):
        raise FileNotFoundError('ProcessJson.lua not found')

    Popen(args=['luajit', os.path.join(settings.POB_SRC, 'ProcessJson.lua')], cwd=settings.POB_SRC).wait()
    return read_xmls()

def read_xmls():
    xmls = []
    for file in glob.glob('*char.xml', root_dir=settings.POB_SRC):
        print(file)
        with open(os.path.join(settings.POB_SRC, file), 'r') as f:
            xmls.append(f.read())
        os.remove(os.path.join(settings.POB_SRC, file))
    return xmls

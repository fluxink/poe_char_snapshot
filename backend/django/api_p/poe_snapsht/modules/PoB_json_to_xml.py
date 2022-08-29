import os
import glob
from subprocess import Popen


LUA_PATH = 'D:\WorkSpace\Projects_edu\PyPDF\LuaJIT\luajit.exe'
LUA_SCRIPT = 'D:\WorkSpace\Projects_edu\PoESandBox\PathOfBuilding\src\ProcessJson.lua'
POB_SRC = 'D:\WorkSpace\Projects_edu\PoESandBox\PathOfBuilding\src'

def send_chars(chars: list):
    with open(os.path.join(POB_SRC, 'CharList.lua'), 'w') as file:
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
    Popen(args=[LUA_PATH, LUA_SCRIPT], cwd=POB_SRC).wait()
    return read_xmls()

def read_xmls():
    xmls = []
    for file in glob.glob('*char.xml', root_dir=POB_SRC):
        print(file)
        with open(os.path.join(POB_SRC, file), 'r') as f:
            xmls.append(f.read())
    return xmls

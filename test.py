import pobapi
from pobapi import constants
url = 'https://pastebin.com/xSvrsMdC'

build = pobapi.from_url(url)

build.xml

stats = {
            constants.STATS_MAP.get(i.get("stat")): float(i.get("value"))
            for i in build.xml.find("Build").findall("PlayerStat")
        }
stats.pop(None, None)


# for stat in stats.items():
#     if stat[1] is not None and stat[1] != 0:
#         print(stat)

print(build.config)
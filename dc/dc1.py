# coding=utf-8
from bs4 import BeautifulSoup
import mechanize
import cookielib
import urllib

from sets import Set
import time
import argparse


MAIN_URL = "https://dragcave.net"
LOC_URL = "https://dragcave.net/locations/"


def setup_mech_browser():
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar("cookies.txt")
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')]

    # ================== #

    #MAIN_URL = "https://dragcave.net"
    #URL = "https://dragcave.net/locations/3"

    cj.load()   # load stored cookies
    #br.open(URL)
    return br

# ================== #

# IMPORTANT NOTE! utf-8 & ascii hell coding. replace ' with ?
EGG_DICT = {
    'gold': "This egg is very reflective, almost metallic-looking.",
    'silver': "This egg gives off a beautiful glow.",
    'aeon': "It?s almost like time is distorted around this egg.",
    'zyu': "This shiny egg seems to radiate power.",
    'floret': "This shiny egg smells faintly like flowers.",
    'purplebluedino': "This egg looks like it doesn?t belong; it is brightly colored with white spots. It?s much lighter than the other eggs.",
    'yellowdino': "This egg looks like it doesn?t belong; it is brightly colored with white spots. It?s much heavier than the other eggs.",
    'greendino': "This egg looks like it doesn?t belong; it is brightly colored with white spots.",
    'reddino': "This egg looks like it doesn?t belong; it is brightly colored with white spots. It?s much warmer than the rest of the eggs.",
    'chicken': "This egg is much smaller than the others.",
    'cheese': "This egg is soft and smells uncannily like cheese.",
    'paper': "This egg is tiny and made out of several pieces of paper folded together.",
    'pyralspite': "This egg feels like polished stone.",
    'copper': "This egg gleams with a reddish shine.",
    'xeno': "Mana courses throughout this glassy egg.",
    'bauta': "This egg has raised golden ridges.",
    'gemshard': "This egg is encrusted with colorful gemstones.",
    'baikala': "This heavy egg has a soft, yielding shell.",
    'truffle': "This egg has a pleasant, musky smell.",

    # holidays - halloween
    'vampire': "This egg is stone cold and smells rotten.",
    'pumpkin': "This egg smells like the autumn harvest.",
    'marrow': "This egg is covered in a dark crust.",
    'shadow': "This egg fades into the shadows.",
    'cavern': "This egg is wedged in a dark corner.",
    'grave': "This egg appears to have an evil grin.",
    'desipis': "Being near this egg makes it hard to think clearly.",
    'caligene': "The pattern on this egg’s shell is unsettling.",
    'witchlight': "This downy egg is hidden in brambles.",
    'omen': "This warm egg is tangled in the roots of a dead tree.",

    # holidays - christmas
    'holly': "This egg has a holly leaf stuck to it.",
    'yulebuck': "This egg is covered with bright, festive stripes.",
    'snowangel': "This egg fills you with holiday cheer.",
    'ribbondancer': "This egg shines like a holiday ribbon.",
    'wintermagi': "This colorful egg is covered by a light layer of snow.",
    'wrappingwing': "This egg has a rich, shiny pattern on it.",
    'solstice': "This egg emits a soft, heartwarming glow.",
    'mistletoe': "This colorful egg gleams in the light.",
    'aegis': "A wintry chill swirls just beneath the surface of this egg.",
    'snow': "This egg is surrounded by frost.",
    'garland': "This festive egg gives off comforting warmth."


}
# 1 = coast, 2 = desert, 3 = forest, 4 = jungle, 5 = alpine, 6 = volcano
ONLY_FROM_LOCATIONS_DICT = {
    'xeno': Set([4]),
    'copper': Set([1, 4]),
    'zyu': Set([4]),
    'floret': Set([3]),
    'baikala': Set([1])
}
# TARGET_EGGS = Set(["This egg is very reflective, almost metallic-looking.",
#                    "This egg gives off a beautiful glow."])
TARGET_EGG_STR_DEFAULT = "gold, silver, xeno, copper, aeon, zyu, purplebluedino, yellowdino, reddino, greendino, chicken, cheese, paper"
# "gold, silver, copper"
# "gold, silver, aeon, baikala"
# "gold, silver, purplebluedino, yellowdino"
# "gold, silver, purplebluedino, yellowdino, reddino, greendino"
# "gold, silver, aeon, copper, purplebluedino, yellowdino, baikala"
# "gold, silver, purplebluedino, yellowdino, xeno, copper, aeon, baikala"
# "gold, silver, chicken, yellowdino, purplebluedino, greendino, reddino"
# "gold, silver, purplebluedino, yellowdino, aeon, xeno, copper, zyumorph"
# "gold, silver, greendino, purplebluedino, yellowdino, reddino, chicken, paper"
# "gold, silver, aeon, copper, zyumorph, yellowdino, purplebluedino, greendino, reddino, chicken"
# "gold, silver, greendino, purplebluedino, yellowdino, reddino, chicken, paper, zyumorph, xeno, copper"
# "gold, silver, greendino, purplebluedino, yellowdino, reddino, chicken, paper, zyumorph, aeon, xeno, copper"


def build_egg_set(string):
    #egg_set = Set()
    egg_dict = {}
    breeds = string.replace(" ", "").split(",")
    for breed in breeds:
        #egg_set.add(EGG_DICT[breed])
        if breed in ONLY_FROM_LOCATIONS_DICT:
            egg_dict[EGG_DICT[breed]] = ONLY_FROM_LOCATIONS_DICT[breed]
        else:
            egg_dict[EGG_DICT[breed]] = None
    #print(egg_set)
    #return egg_set
    print(egg_dict)
    return egg_dict


def location_check(location, skip_set):
    temp = True
    if skip_set:
        if int(location) not in skip_set:
            temp = False
    return temp

# ================== #


def check_eggs(br, target_egg_set, location):
    soup = BeautifulSoup(br.response().read(), "html5lib")
    eggs = soup.find("div", class_="eggs")
    if eggs:
        egg_divs = eggs("div")

        #print(soup.body)
        #print(eggs)
        #print(egg_divs)
        #print(egg_description)

        for egg_div in egg_divs:
            egg_contents = egg_div.contents
            egg_description = egg_contents[2].contents[0]     # egg description
            egg_description = egg_description.encode('ascii', errors='replace')
            egg_link = egg_contents[0]["href"]
            #print(egg_contents)
            print(egg_link + " : " + egg_description)

            if egg_description in target_egg_set:
                claim = location_check(location, target_egg_set[egg_description])
                if claim:
                    #br.open(MAIN_URL+egg_link)
                    print(egg_link)
                    req = br.click_link(url=egg_link)
                    br.open(req)

                    soup2 = BeautifulSoup(br.response().read(), "html5lib")
                    #print(soup2.body)

                    result = None
                    result_msg = "SUCCESS"
                    try:
                        result = soup2.find("img", class_="spr")
                        #result = soup2.find("div", class_="_3p_7")
                    except Exception as e:
                        print(e)
                        pass
                    fail = result is None
                    if fail:
                        result_msg = "FAIL"
                    #print(result)
                    print(result_msg)
                    br.back()
                else:
                    print("SKIPPING")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-l', '--locations', action='store', dest='locations', default="123456",
                        help='Store a simple value')
    parser.add_argument('-p', action='store', dest='pause_time', default=1,
                        help='Store a simple value')
    parser.add_argument('-max', action='store', dest='max_time', default=3600,
                        help='Store a simple value')
    parser.add_argument('-e', action='store', dest='eggs', default="default",
                        help='Store a simple value')
    args = parser.parse_args()

    # LOCATION = "5"
    # PAUSE = 1           # in seconds
    # MAX_TIME = 3600      # in seconds

    ARG_LOCATIONS = str(args.locations)
    LOCATIONS = []
    for letter in ARG_LOCATIONS:
        LOCATIONS.append(letter)
    print(LOCATIONS)
    PAUSE = float(args.pause_time)  # in seconds
    MAX_TIME = float(args.max_time)  # in seconds

    TARGET_EGG_STR = str(args.eggs)
    if TARGET_EGG_STR == "default":
        TARGET_EGG_STR = TARGET_EGG_STR_DEFAULT
    target_egg_set = build_egg_set(TARGET_EGG_STR)

    br = setup_mech_browser()
    # LOOP
    start_time = time.time()
    end_time = start_time
    loc_pause = round(PAUSE/max(1, len(LOCATIONS)), 3)
    print(loc_pause)
    while end_time - start_time < MAX_TIME:
        for location in LOCATIONS:
            br.open(LOC_URL+location, timeout=60)
            check_eggs(br, target_egg_set, location)
            time.sleep(loc_pause)
            end_time = time.time()




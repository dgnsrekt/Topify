from pprint import pprint
from random import choice

# wikipedia = "^1.4.0"

import wikipedia
from wikipedia.exceptions import DisambiguationError

wikipedia.set_lang("en")

ARTIST = "Chris Brown"
ALBUM = "Fortune"

ARTIST = "Lil Wayne"
ALBUM = "A Milli"

ARTIST = "T-Pain"
ALBUM = "Bartender"

ARTIST = "Kanye West"
ALBUM = "Yeezus"

ARTIST = "Travis Scott"
ALBUM = "Astroworld"

ARTIST = "Mitch Murder"
ALBUM = "After Hours"

ARTIST = "Deadmau5"
ALBUM = "Strobe"

ARTIST = "The Rolling Stones"
ALBUM = "Paint It Black"

ARTIST = "The Doors"
ALBUM = "Riders on the Storm"

ARTIST = "Lynyrd Skynyrd"
ALBUM = "Free Bird"

ARTIST = "The Mamas & The Papas"
ALBUM = "California Dreamin"

ARTIST = "The Zombies"
ALBUM = "Time of the Season"

ARTIST = "Aretha Franklin"
ALBUM = "Respect"

ARTIST = "Irene Cara"
ALBUM = "Flashdance"

ARTIST = "Donna Summer"
ALBUM = "Bad Girls"

ARTIST = "Michael Jackson"
ALBUM = "Thriller"

ARTIST = "Van Halen"
ALBUM = "Jump"

ARTIST = "Kenny Loggins"
ALBUM = "Footloose"


ARTIST = "Blondie"
ALBUM = "Call Me"

ARTIST = "Rihanna"
ALBUM = "Talk That Talk"

ARTIST = "Earth, Wind & Fire"
ALBUM = "Chicago"

ARTIST = "Celine Dion"
ALBUM = "My Heart Will Go On"

ARTIST = "Kanye West"
ALBUM = "The Life Of Pablo"

ARTIST = "Huey Lewis & The News"
ALBUM = "The Power Of Love"

ARTIST = "Hans Zimmer"
ALBUM = "Interstellar"

ARTIST = ARTIST.replace("&", "and")
ARTIST_SEARCH = ARTIST + " (musician)"
# ARTIST_SEARCH = ARTIST + " (band)"


search_results = wikipedia.search(ARTIST_SEARCH)

# print(search_results)

search_list = list(filter(lambda item: item.lower() == ARTIST_SEARCH.lower(), search_results))

if len(search_list) < 1:
    # print("nothing found")
    search_list = list(filter(lambda item: item.lower() == ARTIST.lower(), search_results))

if len(search_list) < 1:
    print("Artist not found")
    exit()

search = search_list.pop()
# print(search)

try:
    summary = wikipedia.summary(search, auto_suggest=False)
except DisambiguationError:
    exit()

sentences = summary.split(".")

question_list = list(filter(lambda s: ALBUM.lower() in s.lower(), sentences))

if not question_list:
    print("no questions found.")
    exit()

question = choice(question_list)

STOP_WORDS = ["the"]

for name in ARTIST.lower().split(" "):
    if name in STOP_WORDS:
        continue
    question = question.lower().replace(name, "_" * len(name)).title()

#
#  output = []
#  for word in question.split(" "):
#  for name in ARTIST.lower().split(" "):
#  if name in word.lower():
#  output.append(word.replace(name, "__" * len(word)))
#  print(name, word)
#  else:
#  output.append(word)
#
if question:
    print(question.strip() + ".")
    print()
    print("Who is", ARTIST + "?")
else:
    print("nothing found.")

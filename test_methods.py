from LinkedList import LinkedList, Node

SONGS = [
    {"name": "Blinding Lights",         "artist": "The Weeknd",         "album": "After Hours"},
    {"name": "Bohemian Rhapsody",        "artist": "Queen",              "album": "A Night at the Opera"},
    {"name": "Stairway to Heaven",       "artist": "Led Zeppelin",       "album": "Led Zeppelin IV"},
    {"name": "Hotel California",         "artist": "Eagles",             "album": "Hotel California"},
    {"name": "Smells Like Teen Spirit",  "artist": "Nirvana",            "album": "Nevermind"},
    {"name": "Shape of You",             "artist": "Ed Sheeran",         "album": "Divide"},
    {"name": "Lose Yourself",            "artist": "Eminem",             "album": "8 Mile"},
    {"name": "Billie Jean",              "artist": "Michael Jackson",    "album": "Thriller"},
    {"name": "Rolling in the Deep",      "artist": "Adele",              "album": "21"},
    {"name": "Superstition",             "artist": "Stevie Wonder",      "album": "Talking Book"},
    {"name": "Dreams",                   "artist": "Fleetwood Mac",      "album": "Rumours"},
    {"name": "Crazy in Love",            "artist": "Beyoncé",            "album": "Dangerously in Love"},
    {"name": "Mr. Brightside",           "artist": "The Killers",        "album": "Hot Fuss"},
    {"name": "Redbone",                  "artist": "Childish Gambino",   "album": "Awaken, My Love!"},
    {"name": "Levitating",               "artist": "Dua Lipa",           "album": "Future Nostalgia"},
    {"name": "Good as Hell",             "artist": "Lizzo",              "album": "Cuz I Love You"},
    {"name": "Bad Guy",                  "artist": "Billie Eilish",      "album": "When We All Fall Asleep"},
    {"name": "Peaches",                  "artist": "Justin Bieber",      "album": "Justice"},
    {"name": "Stay",                     "artist": "The Kid LAROI",      "album": "F*CK LOVE 3"},
    {"name": "Montero",                  "artist": "Lil Nas X",          "album": "Montero"},
    {"name": "drivers license",          "artist": "Olivia Rodrigo",     "album": "SOUR"},
    {"name": "Watermelon Sugar",         "artist": "Harry Styles",       "album": "Fine Line"},
    {"name": "Happier Than Ever",        "artist": "Billie Eilish",      "album": "Happier Than Ever"},
    {"name": "Industry Baby",            "artist": "Lil Nas X",          "album": "Montero"},
    {"name": "Heat Waves",               "artist": "Glass Animals",      "album": "Dreamland"},
    {"name": "Shivers",                  "artist": "Ed Sheeran",         "album": "="},
    {"name": "Permission to Dance",      "artist": "BTS",                "album": "Butter"},
    {"name": "Easy On Me",               "artist": "Adele",              "album": "30"},
    {"name": "My Universe",              "artist": "Coldplay",           "album": "Music of the Spheres"},
    {"name": "Butter",                   "artist": "BTS",                "album": "Butter"},
    {"name": "Save Your Tears",          "artist": "The Weeknd",         "album": "After Hours"},
    {"name": "Positions",                "artist": "Ariana Grande",      "album": "Positions"},
    {"name": "Therefore I Am",           "artist": "Billie Eilish",      "album": "Happier Than Ever"},
    {"name": "Mood",                     "artist": "24kGoldn",           "album": "El Dorado"},
    {"name": "Dynamite",                 "artist": "BTS",                "album": "Dynamite"},
    {"name": "Wrecking Ball",            "artist": "Miley Cyrus",        "album": "Bangerz"},
    {"name": "Roar",                     "artist": "Katy Perry",         "album": "Prism"},
    {"name": "Shake It Off",             "artist": "Taylor Swift",       "album": "1989"},
    {"name": "Blank Space",              "artist": "Taylor Swift",       "album": "1989"},
    {"name": "Anti-Hero",                "artist": "Taylor Swift",       "album": "Midnights"},
    {"name": "As It Was",                "artist": "Harry Styles",       "album": "Harry's House"},
    {"name": "About Damn Time",          "artist": "Lizzo",              "album": "Special"},
    {"name": "Running Up That Hill",     "artist": "Kate Bush",          "album": "Hounds of Love"},
    {"name": "Unholy",                   "artist": "Sam Smith",          "album": "Gloria"},
    {"name": "Flowers",                  "artist": "Miley Cyrus",        "album": "Endless Summer Vacation"},
    {"name": "Cruel Summer",             "artist": "Taylor Swift",       "album": "Lover"},
    {"name": "Vampire",                  "artist": "Olivia Rodrigo",     "album": "GUTS"},
    {"name": "Ella Baila Sola",          "artist": "Eslabon Armado",     "album": "Ella Baila Sola"},
    {"name": "La Bebe",                  "artist": "Yng Lvcas",          "album": "La Bebe"},
    {"name": "Quevedo Bzrp Session 52",  "artist": "Bizarrap",           "album": "BZRP Music Sessions"},
]


def load_playlist(ll: LinkedList) -> None:
    for song in SONGS:
        node = Node(name=song["name"], artist=song["artist"], album=song["album"])
        ll.insert_at_end(node)


def display_playlist(ll: LinkedList) -> None:
    print(f"\nPlaylist ({len(ll)} songs):\n")
    for i, node in enumerate(ll, start=1):
        print(f"  {i:>2}. {node.song_data['name']} — {node.song_data['artist']} ({node.song_data['album']})")


if __name__ == "__main__":
    playlist = LinkedList()
    load_playlist(playlist)
    display_playlist(playlist)
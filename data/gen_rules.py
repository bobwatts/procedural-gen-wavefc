
rules = {
    "ocean": ["ocean", "edge ocean"],
    "edge ocean": ["edge ocean", "ocean", "edge beach"],
    "beach": ["edge beach", "beach"],
    "edge beach": ["edge plains", "beach", "edge ocean", "edge beach"],
    "plains": ["edge plains", "plains"],
    "edge plains": [
        "edge plains",
        "edge sparse forest",
        "plains",
        "edge beach",
        "edge mountains",
    ],
    "sparse forest": ["edge sparse forest", "sparse forest"],
    "edge sparse forest": [
        "edge plains",
        "edge sparse forest",
        "sparse forest",
        "edge deep forest",
        "edge mountains",
    ],
    "edge deep forest": [
        "deep forest",
        "edge deep forest",
        "edge sparse forest",
        "edge mountains",
    ],
    "deep forest": ["edge deep forest", "deep forest"],
    "edge mountains": [
        "edge deep forest",
        "edge sparse forest",
        "edge plains",
        "edge mountains",
        "mountains",
    ],
    "mountains": ["mountains", "edge mountains"],
}

loc_rules = {
    "water": ["whirlpool", "sand", "water", "empty"],
    "whirlpool": ["water", "whirlpool", "empty"],
    "sand": ["water", "sand", "empty"],
    "grass": ["grass", "weeds", "tall grass", "moss", "empty"],
    "weeds": ["weeds", "grass", "tall grass", "empty"],
    "tall grass": ["tall grass", "grass", "weeds", "empty"],
    "tree": ["moss", "empty"],
    "moss": ["tree", "moss", "grass", "empty"],
    "large tree": ["moss", "empty"],
    "rock": ["rock", "coal", "iron ore", "gold ore", "empty"],
    "coal": ["rock", "coal", "empty"],
    "iron ore": ["rock", "iron ore", "empty"],
    "gold ore": ["rock", "gold ore", "empty"],
    "empty": ["empty", "water", "whirlpool", "sand","grass",  "weeds", "tall grass","tree","moss","large tree","rock", "coal",  "iron ore" ,"gold ore"  ]
}

biome_loc_rules = {
    "ocean": ["water", "whirlpool", "empty"],
    "edge ocean": ["water", "empty"],
    "beach": ["sand", "empty"],
    "edge beach": ["sand", "empty"],
    "plains": ["grass", "weeds", "tall grass", "empty"],
    "edge plains": ["grass", "weeds", "tall grass", "empty"],
    "sparse forest": ["tree", "moss", "grass", "empty"],
    "edge sparse forest": ["tree", "moss", "grass", "empty"],
    "edge deep forest": ["large tree", "tree", "moss", "empty"],
    "deep forest": ["large tree", "tree", "moss", "empty"],
    "edge mountains": ["rock", "coal", "empty"],
    "mountains": ["rock", "iron ore", "coal", "gold ore", "empty"],
}

tileset = {"biomes": {
    "ocean": "\033[0;34;46m~\033[0;0m",
    "beach": "\033[0;37;43m~\033[0;0m",
    "plains": "\033[0;33;42m'\033[0;0m",
    "sparse forest": "\033[0;33;42mt\033[0;0m",
    "deep forest": "\033[0;32;40mT\033[0;0m",
    "mountains": "\033[0;37;40mM\033[0;0m",
    "edge mountains": "\033[0;37;40mm\033[0;0m",
    "error": "\033[0;35;40mE\033[0;0m",
},
"location": {
    "water": "\033[0;34;46m~\033[0;0m",
    "whirlpool": "\033[0;34;46m0\033[0;0m",
    "sand": "\033[0;37;43m~\033[0;0m",
    "grass": "\033[0;33;42m'\033[0;0m",
    "weeds": "\033[0;33;42m\"\033[0;0m",
    "tall grass": "\033[0;33;42ml\033[0;0m",
    "tree": "\033[0;33;42mt\033[0;0m",
    "moss": "\033[0;33;42m~\033[0;0m",
    "large tree": "\033[0;30;42mT\033[0;0m",
    "rock": "\033[0;37;40mo\033[0;0m",
    "coal": "\033[0;37;40m*\033[0;0m",
    "iron ore": "\033[0;31;40mf\033[0;0m",
    "gold ore": "\033[0;33;40m$\033[0;0m",
    "error": "\033[0;35;40mE\033[0;0m",
},
"backgrounds": {
    "ocean": "\033[0;34;46m~\033[0;0m",
    "beach": "\033[0;37;43m~\033[0;0m",
    "plains": "\033[0;34;43m.\033[0;0m",
    "sparse forest": "\033[0;34;43m.\033[0;0m",
    "deep forest": "\033[0;34;43m.\033[0;0m",
    "mountains": "\033[0;37;40m.\033[0;0m",
    "edge mountains": "\033[0;37;40m.\033[0;0m",
    "error": "\033[0;35;40mE\033[0;0m",
}
}

dark_tileset = {"biomes": {
    "ocean": "\033[0;34;46m~\033[0;0m",
    "beach": "\033[0;37;43m~\033[0;0m",
    "plains": "\033[0;33;42m'\033[0;0m",
    "sparse forest": "\033[0;33;42mt\033[0;0m",
    "deep forest": "\033[0;32;40mT\033[0;0m",
    "mountains": "\033[0;37;40mM\033[0;0m",
    "edge mountains": "\033[0;37;40mm\033[0;0m",
    "error": "\033[0;35;40mE\033[0;0m",
},
"location": {
    "water": "\033[0;34;46m~\033[0;0m",
    "whirlpool": "\033[0;34;46m0\033[0;0m",
    "sand": "\033[0;37;43m~\033[0;0m",
    "grass": "\033[0;32;40m'\033[0;0m",
    "weeds": "\033[0;32;40m\"\033[0;0m",
    "tall grass": "\033[0;32;40ml\033[0;0m",
    "tree": "\033[0;33;40mt\033[0;0m",
    "moss": "\033[0;32;40m~\033[0;0m",
    "large tree": "\033[0;32;40mT\033[0;0m",
    "rock": "\033[0;37;40mo\033[0;0m",
    "coal": "\033[0;37;40m*\033[0;0m",
    "iron ore": "\033[0;31;40mf\033[0;0m",
    "gold ore": "\033[0;33;40m$\033[0;0m",
    "error": "\033[0;35;40mE\033[0;0m",
},
"backgrounds": {
    "ocean": "\033[0;34;46m~\033[0;0m",
    "beach": "\033[0;37;43m~\033[0;0m",
    "plains": "\033[0;37;40m \033[0;0m",
    "sparse forest": "\033[0;37;40m \033[0;0m",
    "deep forest": "\033[0;37;40m \033[0;0m",
    "mountains": "\033[0;37;40m.\033[0;0m",
    "edge mountains": "\033[0;37;40m.\033[0;0m",
    "error": "\033[0;35;40mE\033[0;0m",
}
}

tileset = dark_tileset

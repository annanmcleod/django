from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass
from typing import List
from typing import Dict

# this is my dataclass
@dataclass
class Biome:
    name: str
    description: str
    mobs: list
    plants: list


def home(request):
    biomes = {
        "names": ["Meadow", "Taiga", "Warped_Forest", "Warm_Ocean", "Lush_Caves"],
        "Meadow": Biome(
            "Meadow",
            "On this surface level biome, consists of a grassy area containing patches of different plants and animals. Along the edges or depths, you can find villages to raid and pillager outposts to defeat. If you are looking for a calm, beautiful place to settle in, this is the right place for you.",
            ["Rabbit", "Sheep", "Donkeys"],
            [
                "Allium",
                "Bee Nest",
                "Dandelion",
                "Cornflower",
                "Oxeye Daisy",
                "Azure Bluet",
            ],
        ),
        "Taiga": Biome(
            "Taiga",
            "Among the tall trees surrounding this biome, you can find villages, pillager outposts, a new wolf friend, and berries to eat. If you're desire is to live a wintery world, then you're wish is complete. When it snows, you may even get lucky enough to run across an igloo.",
            ["Wolves", "Foxes", "Sheep", "Pig", "Chicken", "Cow", "Rabbit"],
            ["Fern", "Large Fern", "Sweet Berry Bush"],
        ),
        "Warped_Forest": Biome(
            "Warped Forest",
            "Within this biome of color, as well as haunt, it is possible to see many things you have never seen. In this Nether sub-realm, it is possible to find ruined portals, bastion remnants, and creepy creatures to your heart's delight. Although the essence is fantastic, it is not recommended to settle here, since there are high levels of danger. If you are looking to travel to The End then this is the ideal place to stack up on ender pearls.",
            ["Strider", "Enderman"],
            [
                "Warped Roots",
                "Crimson Roots",
                "Warped Fungus",
                "Crimson Fungus",
                "Nether Sprouts",
                "Twisting Vines",
            ],
        ),
        "Warm_Ocean": Biome(
            "Warm Ocean",
            "In the depths of this biome lies a sandy floor filled with color and shine. Deep into this biome you can find spectacular structures of coral, shipwrecks, and oceanic animals galore. It is not recommended to live in this area as it is underwater, but if you are looking for a new adventure, go right ahead.",
            ["Dolphin", "Squid", "Pufferfish", "Tropical Fish"],
            ["Coral", "Coral Fans", "Sea Pickles", "Seagrass"],
        ),
        "Lush_Caves": Biome(
            "Lush Caves",
            "Deep into an underground world you meet caves with the most extreme humid levels. In your travels you will see dungeons, mine-shafts, strongholds, and other sites to see. This biome is filled to the brim with moss and ores which makes it a treasure trove by the dozen.",
            ["Tropical Fish", "Glow Squid", "Axolotl", "Bat"],
            [
                "Vines",
                "Small Dripleaf",
                "Big Dripleaf",
                "Cave Vines",
                "Spore Blossom",
                "Glow Dirt",
            ],
        ),
    }
    return render(request, "home.html", biomes)


def details(request, input):
    biomes = {
        "minecraft": input,
        "Meadow": Biome(
            "Meadow",
            "On this surface level biome, consists of a grassy area containing patches of different plants and animals. Along the edges or depths, you can find villages to raid and pillager outposts to defeat. If you are looking for a calm, beautiful place to settle in, this is the right place for you.",
            ["Rabbit", "Sheep", "Donkeys"],
            [
                "Allium",
                "Bee Nest",
                "Dandelion",
                "Cornflower",
                "Oxeye Daisy",
                "Azure Bluet",
            ],
        ),
        "Taiga": Biome(
            "Taiga",
            "Among the tall trees surrounding this biome, you can find villages, pillager outposts, a new wolf friend, and berries to eat. If you're desire is to live a wintery world, then you're wish is complete. When it snows, you may even get lucky enough to run across an igloo.",
            ["Wolves", "Foxes", "Sheep", "Pig", "Chicken", "Cow", "Rabbit"],
            ["Fern", "Large Fern", "Sweet Berry Bush"],
        ),
        "Warped_Forest": Biome(
            "Warped Forest",
            "Within this biome of color, as well as haunt, it is possible to see many things you have never seen. In this Nether sub-realm, it is possible to find ruined portals, bastion remnants, and creepy creatures to your heart's delight. Although the essence is fantastic, it is not recommended to settle here, since there are high levels of danger. If you are looking to travel to The End then this is the ideal place to stack up on ender pearls.",
            ["Strider", "Enderman"],
            [
                "Warped Roots",
                "Crimson Roots",
                "Warped Fungus",
                "Crimson Fungus",
                "Nether Sprouts",
                "Twisting Vines",
            ],
        ),
        "Warm_Ocean": Biome(
            "Warm Ocean",
            "In the depths of this biome lies a sandy floor filled with color and shine. Deep into this biome you can find spectacular structures of coral, shipwrecks, and oceanic animals galore. It is not recommended to live in this area as it is underwater, but if you are looking for a new adventure, go right ahead.",
            ["Dolphin", "Squid", "Pufferfish", "Tropical Fish"],
            ["Coral", "Coral Fans", "Sea Pickles", "Seagrass"],
        ),
        "Lush_Caves": Biome(
            "Lush Caves",
            "Deep into an underground world you meet caves with the most extreme humid levels. In your travels you will see dungeons, mine-shafts, strongholds, and other sites to see. This biome is filled to the brim with moss and ores which makes it a treasure trove by the dozen.",
            ["Tropical Fish", "Glow Squid", "Axolotl", "Bat"],
            [
                "Vines",
                "Small Dripleaf",
                "Big Dripleaf",
                "Cave Vines",
                "Spore Blossom",
                "Glow Dirt",
                "Hanging ",
            ],
        ),
    }
    return render(request, "details.html", biomes)

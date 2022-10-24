from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass
from typing import List
from typing import Dict

# this is my dataclass
@dataclass
class Team:
    name: str
    description: str
    members: list


def home(request):
    teams = {
        "names": ["Management", "Procurement", "Documentation", "Community"],
        "Management": Team(
            "Management",
            "The management team consists of a group who.",
            ["Brooks", "Chevy", "Errin", "Kevin", "Lukas", "Andrew"],
        ),
        "Procurement": Team(
            "Procurement",
            "The procurement team consists of a group who.",
            ["Mike", "Dylan", "Anna", "Zaul", "Luke", "River"],
        ),
        "Documentation": Team(
            "Documentation",
            "The documentation team consists of a group who.",
            ["Colt", "Isaiah", "Cooper", "Cannon", "Angela", "Antonio", "Gabriel"],
        ),
        "Community": Team(
            "Community",
            "The community team consists of a group who.",
            ["Joshua", "Malcolm", "Amber", "J.W", "Eric"],
        ),
    }
    return render(request, "home.html", teams)


def details(request, input):
    teams = {
        "something": input,
        "Management": Team(
            "Management",
            "The management team consists of a group of people who make sure everything at Base Camp is running smoothly. By giving out chore plans and assigning dates for deep cleans, proper functioning at Base Camp will never fail.",
            ["Errin", "Kevin", "Lukas", "Chevy", "Brooks", "Andrew"],
        ),
        "Procurement": Team(
            "Procurement",
            "The procurement team consists of a group of people who supply the food and other kitchen necessities. On the days where Base Camp wants to eat something special for lunch, this team is in charge.",
            ["Zaul", "Anna", "Mike", "Luke", "River", "Dylan"],
        ),
        "Documentation": Team(
            "Documentation",
            "The documentation team consists of a group of people who keep up with the social media at Base Camp Coding Academy. Anytime we have an event going on, Documentation is sure to capture it and then post it to the official BCCA accounts. Check out the Instagram, Facebook, and Twitter.",
            ["Colt", "Isaiah", "Angela", "Cooper", "Gabriel", "Cannon", "Antonio"],
        ),
        "Community": Team(
            "Community",
            "The community team consists of a group of people who plan all special events such as bowling, board games, karaoke, and grill-out days. Along with planning these days, this team also makes sure everyone's birthday is celebrated the best day.",
            ["J.W", "Eric", "Joshua", "Amber", "Malcolm"],
        ),
    }
    return render(request, "details.html", teams)

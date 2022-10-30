import io
import json
import random

# noinspection PyUnresolvedReferences
import pyodide


class Subject:
    # noinspection PyDefaultArgument
    def __init__(self, data={}):
        self.name: str = data.get('name')
        self.quote: str = data.get('quote')
        self.title: str = data.get('title')
        self.images: str = data.get('images')
        self.main: str = data.get('main')
        self.secondary: str = data.get('secondary')


def get_random_subject() -> dict:
    subjects = [
        {
            'name': 'Zaha hadid',
            'quote': "I don't think that architecture is only about shelter, is only about a very simple enclosure.\
                It should be able to excite you, to calm you, to make you think.",
            'title': 'Heydar Aliyev Cultural Center',
            'images': 'zh',
            'main': '#1B365E',
            'secondary': '#90B6DE',
        },
        {
            'name': 'Bjarke Ingels',
            'quote': "In the big picture, architecture is the art and science \
                of making sure that our cities and buildings fit with the way we want to live our lives.",
            'title': 'Kistefos Museum Norway',
            'images': 'bi',
            'main': '#01293D',
            'secondary': '#97B5D9',
        },
        {
            'name': 'Jean Nouvel',
            'quote': "Architecture is always an answer given to a question that is not asked!",
            'title': 'National Museum of Qatar',
            'images': 'jn',
            'main': '#795731',
            'secondary': '#E5C489',
        },
        {
            'name': 'Ieoh Ming Pei',
            'quote': "Architecture is the very mirror of life. \
                You only have to cast your eyes on buildings to feel the presence of the past, \
                    the spirit of a place; they are the reflection of society.",
            'title': 'The pyramid of Louvre',
            'images': 'imp',
            'main': '#1F305C',
            'secondary': '#E6D7B0',
        },
        {
            'name': 'Frank Gehry',
            'quote': "Architecture should speak of its time and place, but yearn for timelessness.",
            'title': 'La Tour - Luma Fondation',
            'images': 'fg',
            'main': '#4A2E1E',
            'secondary': '#F2D2A7',
        },
    ]

    return random.choice(subjects)

def download_subject() -> Subject:
    forecast: dict = get_random_subject()

    return Subject(forecast)

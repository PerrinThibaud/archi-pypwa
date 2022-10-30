# noinspection PyUnresolvedReferences
import random

# noinspection PyUnresolvedReferences,PyPackageRequirements
import pyodide
# noinspection PyUnresolvedReferences,PyPackageRequirements
from js import DOMParser, document, setInterval, console

# noinspection PyPackages
import subject_api

# noinspection PyPackages
from subject_api import Subject


def main():
    set_theme()
    add_refresh_event()


def set_theme():
    body = document.getElementById('body')
    div_content = document.getElementById('content')
    div_name_architect = document.getElementById('name_architect')
    div_quote_architect = document.getElementById('quote_architect')
    div_architect = document.getElementById('architect')
    div_architecture = document.getElementById('architecture')
    div_title = document.getElementById('title_architect')

    add_class(div_content, 'hidden')
    add_class(div_architect, 'hidden')

    try:
        forecast: Subject = subject_api.download_subject()
    except Exception as x:
        console.log("Error calling weather API: {}".format(x))
        forecast = create_error_style_report()
    body.style.setProperty("--main-color", forecast.main)
    body.style.setProperty("--secondary-color", forecast.secondary)
    div_name_architect.innerText = forecast.name
    div_title.innerText = forecast.title
    div_quote_architect.innerText = f"\"{forecast.quote}\""
    div_architect.children[0].setAttribute('src', '/static/images/architects/{}.webp'.format(forecast.images))
    div_architecture.children[1].setAttribute('src', '/static/images/architecture/{}.webp'.format(forecast.images))

    remove_class(div_content, 'hidden')
    remove_class(div_architect, 'hidden')


def create_error_style_report():
    forecast = Subject()
    forecast.name = 'Offline'
    forecast.quote = 'Quote API is offline.'
    forecast.title = 'offline'
    forecast.images = 'offline'
    forecast.main = '#762635'
    forecast.secondary = '#F3A6D0'
    return forecast


def add_refresh_event():
    def evt(e=None):
        set_theme()
        if e:
            e.preventDefault()
        return False

    refresh_link = document.getElementById('refresh')
    refresh_link.onclick = evt


def remove_class(element, class_name):
    element.classList.remove(class_name)


def add_class(element, class_name):
    element.classList.add(class_name)


try:
    main()
except Exception as x:
    print("Error starting weather script: {}".format(x))

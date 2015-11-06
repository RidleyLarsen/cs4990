import requests
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from .models import Pin


def get_image_url(sender, instance, **kwargs):
    response = requests.get(instance.link)
    try:
        if response.status_code == 200:
            html = BeautifulSoup(response.text)
            image = html.find('meta', property="og:image")
            url = image.get('content')
            if url:
                instance.image_url = url

            description = html.find('meta', property="og:description")
            if description:
                instance.description = description.get('content')

            title = html.find('meta', property="og:title")
            if title:
                instance.title = title.get('content')
    except:
        raise ValidationError("Couldn't get an OpenGraph image from the link.")

pre_save.connect(get_image_url, sender=Pin)

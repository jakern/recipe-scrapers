import requests

from recipe_scrapers.settings import settings

from ._abstract import AbstractScraper
from ._utils import url_path_to_dict

# some sites close their content for 'bots', so user-agent must be supplied
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}


class EatThisMuch(AbstractScraper):
    def __init__(self, url, *args, **kwargs):
        if not settings.TEST_MODE:
            target = url_path_to_dict(url)["path"].split("/")[-1].split(",")[-1]
            api_url = f"https://www.eatthismuch.com/api/v1/recipe/{target}/"
            api_data = requests.get(api_url, headers=HEADERS).json()
        else:
            import json

            api_data = json.loads(url.read())

        super().__init__(url=url, *args, **kwargs)

        self.author = api_data.get("uploader")
        self.title = api_data.get("food_name")
        self.category = ""
        self.total_time = api_data.get("total_time")
        self.yields = api_data.get("number_servings")
        self.image = api_data.get("default_image").get("image")
        self.ingredients = [
            ingredient.get("food").get("food_name")
            for ingredient in api_data.get("ingredients")
        ]
        self.instructions = [
            instruction.get("text") for instruction in api_data.get("directions")
        ]
        self.ratings = api_data.get("food_rating")
        self.cuisine = ""
        self.description = api_data.get("description")

    @classmethod
    def host(cls):
        return "eatthismuch.com"

    def canonical_url(self):
        return self.url

    def author(self):
        return self.author

    def title(self):
        return self.title

    def category(self):
        return self.category

    def total_time(self):
        return self.total_time

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.image

    def ingredients(self):
        return self.ingredients

    def instructions(self):
        return self.instructions

    def ratings(self):
        return self.ratings

    def cuisine(self):
        return self.cuisine

    def description(self):
        return self.description

from recipe_scrapers.eatthismuch import EatThisMuch
from tests import ScraperTest


class TestEatThisMuchScraper(ScraperTest):

    scraper_class = EatThisMuch

    def test_host(self):
        self.assertEqual("eatthismuch.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("deleted_78202", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Baked Egg Rolls", self.harvester_class.title())

    def test_category(self):
        self.assertEqual(None, self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(8, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://images.eatthismuch.com/site_media/img/56896_tabitharwheeler_bd29b621-991d-4d7f-8816-e99b06967f6c.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "1/2 cup, chopped Cabbage",
                "1/4 cup grated Carrots",
                "1 tbsp Soy sauce",
                "2 clove Garlic",
                '8 wrapper, eggroll (7" square) Wonton wrappers',
                "1 large Egg",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        # self.assertEqual("['Makes 4 steaks, assuming each steak is about 7oz (220g).', 'Place butter in a mixing bowl and using a fork, beat until soft. Add crushed garlic and chopped scallions (spring onions) and mix.', 'Spoon butter mixture onto plastic wrap and roll into a log cylindrical shape. Refrigerate until firm (15 min).', 'Heat a frying pan over medium heat for 3-4 minutes until hot. Brush meat with olive oil and sprinkle with pepper.', 'Place steaks in frying pan and cook without turning until juices rise to uncooked side, 1-2 minutes. Then turn over and cook to your liking, 1 more minute for medium-rare or 2 minutes for medium to well-done.', 'Place steaks on serving plates, cut garlic butter into quarters and place one on each steak. Serve with a salad.']", self.harvester_class.instructions())
        self.assertEqual("", self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(None, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(None, self.harvester_class.cuisine())

    def test_description(self):
        self.assertEqual(None, self.harvester_class.description())

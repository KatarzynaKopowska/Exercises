import requests
import collections


JobOffer = collections.namedtuple(
    "JobOffer", ("position", "company", "url", "salary", "source"),
)


class NoFluffJobsScraper:
    url = "https://nofluffjobs.com/api/search/posting"
    data_class = JobOffer

    def get_offers(self):
        return requests.get(self.url).json()["postings"]

    def parse_offer(self, offer):
        data = {
            "position": offer.get("title"),
            "company": offer.get("name"),
            "url": offer.get("url"),
            "source": "nofluffjobs",
            "salary": "-",
        }

        return self.data_class(**data)


class JustJoinItScraper:
    url = "https://justjoin.it/api/offers"
    data_class = JobOffer

    def get_offers(self):
        return requests.get(self.url).json()

    def parse_offer(self, offer):
        data = {"position": offer.get("title"),
                "company": offer.get("company_name"),
                "salary": "{} - {}".format(offer.get("salary_from"), offer.get("salary_to")),
                "url": "-",
                "source": "justjoinit",
                }

        return self.data_class(**data)


class Scraper:
    scraper_classes = (NoFluffJobsScraper, JustJoinItScraper)

    def __init__(self):
        self.offers = []

    def run(self, filter_position=None):
        for scraper_class in self.scraper_classes:
            scraper = scraper_class()
            for offer_data in scraper.get_offers():
                offer = scraper.parse_offer(offer_data)
                if filter_position and filter_position in offer.position.lower():
                    self.offers.append(offer)
        return self.offers


scraper = Scraper()
scraper.run(filter_position="python")


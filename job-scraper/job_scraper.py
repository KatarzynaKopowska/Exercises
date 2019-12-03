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


nfjs = NoFluffJobsScraper()
for offer_data in nfjs.get_offers():
    offer = nfjs.parse_offer(offer_data)
    print(offer)

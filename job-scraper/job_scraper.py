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
        data = {"position": offer.get("titile"),
                "company": offer.get("company_name"),
                "salary": "{} - {}".format(offer.get("salary_from"), offer.get("salary_to")),
                "url": "-",
                "source": "justjoinit",
                }

        return self.data_class(**data)



# class Scraper:
#     scraper_classes = (NoFluffJobsScraper, JustJoinItScraper)
#
# jji = JustJoinIt()
# x = jji.get_offers()
# print(x)
# nfjs = NoFluffJobsScraper()
# y = nfjs.get_offers()
# print(type(y))
# # for offer_data in nfjs.get_offers():
# #     offer = nfjs.parse_offer(offer_data)
# #     print(offer)

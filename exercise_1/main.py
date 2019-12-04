from job_scraper import ServicesScraperManager


scraper_manager = ServicesScraperManager()
python_offers = scraper_manager.run(filter_position="python")
for offer in python_offers:
    print(f"{offer.position}, {offer.url}, {offer.salary}")

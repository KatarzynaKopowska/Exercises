from job_scraper import JobScraper
import config

if __name__ == '__main__':
    js = JobScraper()
    page = [config.just_join, config.no_fluff]
    counter = 0
    for name in page:
        data = js.get_url(name)
        if type(data) == dict:
            key = list(data.keys())[0]
            data = data[key]

            for job in data:
                offer = js.find_python_job(job, config.technology)
                if offer:
                    print(offer[1][config.title])
                    counter += 1

        elif type(data) == list:
            for job in data:
                offer = js.find_python_job(job, config.technology)
                if offer:
                    print(offer[1][config.title])
                    counter += 1

    print('Found job ' + str(counter))

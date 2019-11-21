import requests


class JobScraper:

    @staticmethod
    def get_url(URL):
        r = requests.get(url=URL)
        data = r.json()
        return data

    @staticmethod
    def find_python_job(data, value):
        for k, v in data.items():
            if type(v) == str and value in v.lower():
                return True, data
            else:
                pass

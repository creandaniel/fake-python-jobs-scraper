from bs4 import BeautifulSoup
import requests
from time import sleep

class FakeJobsScraper:
    def __init__ (self):
        self.url = "https://realpython.github.io/fake-jobs"
       
    def scrape_data(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "html.parser")

        self.job_elements = soup.find_all("div", class_="card-content")

        for job_element in self.job_elements:

            d = dict()
            d['title_element'] = job_element.find("h2", class_="title")
            d['company_element'] = job_element.find("h3", class_="subtitle")
            d['job_element'] = job_element.find("p", class_="is-small")

            data = []
            data.append(d)
            
            self.display_data(data)


        # sleep(10)
    def display_data(self, data):
        for d in data:
            print(d['title_element'])
            print(d['company_element'])
            print(d['job_element'])


s = FakeJobsScraper()

print(s.scrape_data())

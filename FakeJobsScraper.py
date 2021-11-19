from bs4 import BeautifulSoup
import requests
from urllib.error import URLError
from time import sleep
import json
import os.path

class FakeJobsScraper:
    def __init__ (self):
        self.url = "https://realpython.github.io/fake-jobs"


       
    def scrape_data(self):
        try:
            req = requests.get(self.url)
            req.raise_for_status()
        except URLError as ue:
            print("The Server Could Not be Found")
        else: 

            soup = BeautifulSoup(req.text, "html.parser")

            self.job_elements = soup.find_all("div", class_="card-content")
            data = []
            for job_element in self.job_elements:

                d = dict()
                d['title_element'] = job_element.find("h2", class_="title").text.strip()
                d['company_element'] = job_element.find("h3", class_="subtitle").text.strip()
                d['job_element'] = job_element.find("p", class_="is-small").text.strip()
                
                data.append(d)
                self.save_json(data)
                #self.display_data(data)


        # sleep(10)
    def display_data(self, data):
        for d in data:
            print(d['title_element'])
            print(d['company_element'])
            print(d['job_element'])
    
    
    def save_json(self,data):
        with open("textbooks.json", "w") as writeJSON:
            json.dump(data, writeJSON, ensure_ascii=False, indent=4)

    def open_json(self):
        f = open('textbooks.json',)
        data = json.load(f)

        for i in data:
            print(i['title_element'])
            print(i['company_element'])
            print(i['job_element'])

        f.close()

s = FakeJobsScraper()

if os.path.exists('textbooks.json'):
    print(s.open_json())
    print("file exsists")
else:
    print(s.scrape_data())
    print("file doesn't exsist so we wcrape the data")

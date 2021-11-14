from bs4 import BeautifulSoup
import requests

class FakeJobsScraper:
    def __init__ (self):
        self.url = "https://realpython.github.io/fake-jobs"
       
    def scrape_data(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "html.parser")

        self.job_elements = soup.find_all("div", class_="card-content")

        for job_element in self.job_elements:
            self.title_element = job_element.find("h2", class_="title")
            self.company_element = job_element.find("h3", class_="subtitle")
            self.date_element = job_element.find("p", class_="is-small")
            print(
                  "Job Title: " + self.title_element.text.strip() + 
                  " Company: " + self.company_element.text.strip() + 
                  " Date Posted: " + self.date_element.text.strip()
                 )
        

s = FakeJobsScraper()

print(s.scrape_data())


    






from bs4 import BeautifulSoup
import requests
import lxml
import json

base_url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.5435361040039%2C%22east%22%3A-122.3231228959961%2C%22south%22%3A37.730502526148875%2C%22north%22%3A37.82005426366691%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A572818%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
address = []
price = []
links = []


class Houseinfo:

    def __init__(self) -> None:
        self.address = address
        self.price = price
        self.links = links
        self.response = requests.get(base_url,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50","Accept-Language":"en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7"})
        self.content = self.response.text
        self.get_info()
        

    
    def get_info(self):
        self.soup = BeautifulSoup(self.content,"lxml")
        self.locations = self.soup.find_all(name='a',class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link")
        self.amounts = self.soup.find_all(name="div", class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 bqsBln")
        self.urls = self.soup.find_all(name="a",class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link")
        for location in self.locations:
            address.append(location.address.text)
        for amount in self.amounts:
            l1 = []
            l1[:0] = amount.span.text
            l2 = l1[1:6]
            pr = ' '
            l2.remove(',')
            for i in l2:
                pr += i
            price.append(pr)
        for url in self.urls:
            hp = url["href"]
            self.links.append(hp)
        
        
        return self.address,self.price,self.links



# house_details = Houseinfo()
# # print(house_details.address)
# # print(house_details.price)

# print(house_details.get_info())



#Web Scraper for Oyo Hotels
import requests
from bs4 import BeautifulSoup
import pandas

req = requests.get(oyo_url)
content = req.content

soup = BeautifulSoup(content, "html.parser")

all_hotels = soup.find_all("div", {"class": "hotelCardListing"})

scaped_info_list = []

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore"

for hotel in all_hotels:
    hotel_dict = {}
    hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
    hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
    hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalPrice"}).text

    #try .... except
    try:
        hotel_dict["rating"] = hotel.find("div", {"class": "amenityWrapper"})
    except AttributeError:
        pass

dataFrame = pandas.DataFrame(scraped_info_list)
#dataFrame.to_csv("oyo.csv")
print(name, address, price, rating)

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

Product_Name=[]
Prices=[]
Description=[]
Reviews=[]

for i in range(2,8):
    url="https://www.flipkart.com/search?q=mobiles+under+30000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+30000%7CMobiles&requestId=9d5620bd-18c0-4c21-9788-f63a2e2cd4bd&as-backfill=on&page=1"

    data=requests.get(url)

    soup = BeautifulSoup(data.text, "html.parser")
    box = soup.find("div", class_="DOjaWF gdgoEp")

    names = box.find_all('div', class_='KzDlHZ')
    for i in names:
        name = i.text
        Product_Name.append(name)
    #print(Product_Name)

    prices = box.find_all('div', class_='Nx9bqj _4b5DiR')
    for i in prices:
        name=i.text
        Prices.append(name)
    #print(Prices)

    desc = box.find_all('ul', class_='G4BRas')
    for i in desc:
        name = i.text
        Description.append(name)
    #print(Description)

    reviews = box.find_all('div', class_='XQDdHH')
    for i in reviews:
        name = i.text
        Reviews.append(name)
    #print(Reviews)


data_frame = pd.DataFrame({"Product Name":Product_Name, "Prices":Prices, "Descriptions":Description, "Reviews":Reviews})
print(data_frame)
data_frame.to_csv("web_scraper_on_flipkart.csv")






    
   
    







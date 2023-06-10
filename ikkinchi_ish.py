import requests
import re
import pandas
from bs4 import BeautifulSoup



def get_listed_data(url_list):
    scraped_data = []
    for url in url_list:
        print("URL...", url, type(url))
        re = requests.get(url.get("url"))
        soup = BeautifulSoup(re.content, 'html.parser')
        lis = soup.find_all('li', class_="s-item s-item__pl-on-bottom")    
        for i in lis[1:]:
            title = i.find("span", attrs={"role": "heading"})
            price = i.find("span", class_="s-item__price")
            scraped_data.append(
                {
                    "title": title.text.strip().replace(",", '.'),
                    "price": price.text.strip().replace("$", "")
                }
            )
    return scraped_data

url = "https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0"
re = requests.get(url)
soup = BeautifulSoup(re.content, 'html.parser')
element=soup.find("ol", class_="pagination__items").find_all("li")
url_list=[]
for li in element:
    a_tag=li.find('a')
    url_list.append(
        {
            "url": a_tag.get("href")
        }
    )
scraped_data= get_listed_data(url_list)

df = pandas.DataFrame(data=scraped_data)
df.to_excel('sampl.xlsx', index=False)
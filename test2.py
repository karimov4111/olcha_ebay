import requests
import pandas
from bs4 import BeautifulSoup

url = "https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0"
re = requests.get(url)
soup = BeautifulSoup(re.content, 'html.parser')
lis = soup.find_all('li', class_="s-item s-item__pl-on-bottom")
scraped_data = []
for i in lis[1:]:
    title = i.find("span", attrs={"role": "heading"})
    price = i.find("span", class_="s-item__price")
    scraped_data.append(
        {
            "title": title.text.strip().replace(",", '.'),
            "price": price.text.strip().replace("$", "")
        }
    )
    print(scraped_data)
df = pandas.DataFrame(data=scraped_data)
df.to_excel('sa.xlsx', index=False)
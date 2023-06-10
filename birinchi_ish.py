import requests
import pandas
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook

url="https://olcha.uz/oz/search?q=apple%20airpods&page=4"

re=requests.get(url)

soup=BeautifulSoup(re.content, "html.parser")

list0=soup.find_all("div", class_="product-card__content")


screap_data=[]

for i in list0:
    title = i.find("div", class_="product-card__brand-name")
    narx = i.find("div", class_="price__main")
    print(narx.text)
    screap_data.append(
        {
            "title": title.text,
            "narx": narx.text
        }
    )

df=pandas.DataFrame(data=screap_data)
df.to_excel('sample.xlsx', index=False)
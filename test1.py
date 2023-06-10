import requests
import pandas
from bs4 import BeautifulSoup

all_url=[f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&rt=nc&_pgn=1,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&rt=nc&_pgn=2,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&rt=nc&_pgn=3,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&rt=nc&_pgn=4,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&_pgn=5&rt=nc,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&_pgn=6&rt=nc,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&_pgn=7&rt=nc,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&_pgn=8&rt=nc,"
        f"https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0&_pgn=9&rt=nc"]

for url in all_url:  
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'html.parser')
    lis = soup.find_all('li', class_="s-item s-item__pl-on-bottom")
    scraped_data = []
    for i in lis[1:]:
        title = i.find("span", attrs={"role": "heading"})
        price = i.find("span", class_="s-item__price")
        scraped_data.append(
            {
                "title": title.text,
                "price": price.text
            }
        )
        df = pandas.DataFrame(data=scraped_data)
        df.to_excel('sample.xlsx', index=False)


    
from bs4 import BeautifulSoup
import requests
import pandas as pd

books = []

for page_num in range(1,2):
    print("page switched=",page_num)

    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    page = requests.get(url)

    soup1 = BeautifulSoup(page.content,'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    ol = soup2.find('ol')

    articles = ol.find_all('article',class_ = 'product_pod')

    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']

        star = article.find('p')
        star = star['class'][1]
        price = article.find('p',class_= 'price_color').text.strip()
        price = float(price[1:])

        books.append([title,price,star])




df = pd.DataFrame(books,columns=['Title','price','star rating'])
df.to_csv("C:\\Users\\abdoo\\OneDrive\\Desktop\\books.csv")
print(df)

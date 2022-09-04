# Libraries import
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set the path to chromedriver to configure webdriver to use Chrome browser
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

# Create empty lists to store data fetched from the specified URL
products = []
prices = []
ratings = []

# Specify the URL to fetch data from
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=search.flipkart.com%2C6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
# driver.get("<a href='https://www.flipkart.com/laptops/'></a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")
# driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")


# Scraping the data from the website referencing the tags in which the data are enclosed in
content = driver.page_source
soup = BeautifulSoup(content)
# for a in soup.findAll('a', href=True, attrs={'class':'_31qSD5'}):
for a in soup.findAll('a', attrs={'class':'_1AtVbE'}):
    # name = a.find('div', attrs={'class': '_3wU53n'})
    name = a.find('a', attrs={'class': 's1Q9rs'})
    # price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    price = a.find('div', attrs={'class': '_30jeq3'})
    # rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

# Storing the extracted data in preferred format
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')

# Print the extracted data
x = pd.read_csv('/products.csv')

print(x)
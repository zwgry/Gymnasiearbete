import requests
from requests import get
from bs4 import BeautifulSoup
#from my_server import db
#from my_server.models import Category, Product

url = "https://www.inet.se/kategori/30/bildskarm"
headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

#initiate data storage


result = soup.find_all('picture')

"""for container in result:
    #new_product = Product(name=container.a.h4.text,description=f'desc{container.a.h4.text}',stock=10,category=12,price=12)
    #db.session.add(new_product)
    print(container.find('img')['src'])"""

#db.session.commit()

"""for container in result:
    new_product = Product(name=container.a.h4.text,description=f'desc{container.a.h4.text}',stock=10,category=1,price=12)
    db.session.add(new_product)
    print(container.a.h4.text)
db.session.commit()"""

"""result = soup.find_all('span', class_='name')

#our loop through each container
for container in result:
    new_category = Category(name=container.text,description=f'des{container.text}',super_category=None)
    db.session.add(new_category)
    print(container.text)
db.session.commit()"""
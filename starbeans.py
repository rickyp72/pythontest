import urllib
import time

def get_price():
    page = urllib.urlopen("http://www.silvercoinsbullion.co.uk")
    text = page.read()
    where = text.find('pound')
    start_of_price = where + 6
    end_of_price = start_of_price + 5
    price = float(text[start_of_price:end_of_price])

price = float(99.99)
while price > 23.00:
   # time.sleep(10)
    get_price()
print(price)
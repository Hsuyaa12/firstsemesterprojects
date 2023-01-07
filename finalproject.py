import requests
from IPython.utils.sysinfo import pprint
from ast import Param
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import matplotlib.pyplot as plt
import numpy as np

urls = ['https://www.investing.com/crypto/bitcoin', 'https://www.investing.com/crypto/ethereum', 'https://www.investing.com/crypto/tether', 'https://www.investing.com/crypto/bnb', 'https://www.investing.com/crypto/usd-coin']

for url in urls:
  params = {'api_key': '864221d4c815cd2b40980b36732daf4c', 'url': url}

  page = requests.get('http://api.scraperapi.com/', params=urlencode(params))
  soup = BeautifulSoup(page.text, 'html.parser')
  def Name():
    companyName = soup.find('h1', {'class': 'float_lang_base_1 relativeAttr'}).text
    return companyName

  def Price():
    StockPrice = soup.find('div', {'class': 'top bold inlineblock'}).find_all('span')[1].text
    return StockPrice

  def changeInPrice():
    changeInPrice = soup.find('div', {'class': 'top bold inlineblock'}).find_all('span')[2].text
    return changeInPrice
  print('\n')
  userAnswer = int(input("What do you want to see for"+" "+ Name() + "\n1. Current Price\n2. Recent Change in Price\n3. Both\n"))
  if (userAnswer == 1):
    print('Current Price: $',Price())
  elif(userAnswer == 2):
    print('Recent Change in Price: $', changeInPrice())
  elif(userAnswer == 3):
    print('Current Price: $',Price())
    print('Recent Change in Price: $', changeInPrice())
  else:
    print("Invalid! you entered number other than 1 and 2.")

print("\n")
print("-----------PIE CHART FOR TOP 5 MARKET CAPITAL CRYTOCURRENCY-----------")
print("\n")
plt.figure(figsize=(8,10))
y = [316.41, 147.37, 65.3, 48.29, 43.82]
myLabels = ["Bitcoin", "Etherum", "Tether", "BNB", "USD"]

plt.pie(y, labels=myLabels, autopct=lambda p:f'{p:.2f}%, {p*sum(y)/100.0 :.0f} Billion')
plt.show()

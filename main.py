from bs4 import BeautifulSoup
import sys
import requests
from selenium import webdriver
import time
import csv


driver = webdriver.Firefox()
url = 'https://www.industrybuying.com/'
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, "html.parser")


firstitem = soup.find(class_='thumbPro')


headings = soup.find_all(class_='heading')
products = soup.find_all(class_='thumbPro')



# i = 0

f = csv.writer(open("ib_items.csv", "w"))
f.writerow(["Headings", "Name", "Brand", "Price", "Old_price"])

for heading in headings:
    # i += 1
    # if i == 3:
    #     sys.exit(0)
    print('\n ---------------- \n ')
    headingformat = heading.get_text().strip()
    print(headingformat)
    print('\n ---------------- \n ')
    print('Waiting 5 Seconds')
    time.sleep(5)
    for product in products:
        time.sleep(1)
        try:
            Nameofproduct = product.find(class_='proSpec').get_text().strip()
            print('\nNameofproduct:{}'.format(Nameofproduct))
        except Exception as e:
            Nameofproduct = "N/A"
            print('N/A')
            print('\n')
            pass
        try:
            Brand = product.div.a.div.contents[3].span.get_text().strip().replace(" ", "")
            Brand = ''.join(Brand.split())
            print('\nBrand:{}'.format(Brand))
        except Exception as e:
            Brand = "N/A"
            print('N/A')
            print('\n')
            pass

        try:
            mainPrice = product.find(class_='mainPrice').get_text().strip().replace(" ", "")
            mainPrice = ''.join(mainPrice.split())
            print('\nmainPrice:{}'.format(mainPrice))
        except Exception as e:
            mainPrice = "N/A"
            print('N/A')
            print('\n')
            pass

        try:
            old_price = product.div.a.find(class_='lowerSection').stroke.get_text().strip().replace(" ", "")
            old_price = ''.join(old_price.split())
            print('Old_price:{}'.format(old_price))
        except Exception as e:
            old_price = "N/A"
            print('N/A')
            print('\n')
            pass

        f.writerow([headingformat, Nameofproduct, Brand, mainPrice, old_price])

        print('\n')
        print('\n')

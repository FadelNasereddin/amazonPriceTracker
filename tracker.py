import requests #Accesses URL
from bs4 import BeautifulSoup as bs 
import smtplib
import time 

URL='https://www.amazon.ca/Keurig-K-Select-Coffee-Maker-Matte/dp/B07B8SQXLK/ref=sr_1_1_sspa?crid=3M68BKCL5AGLC&keywords=keurig+coffee+maker&qid=1584239335&sprefix=keurgi%2Caps%2C272&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0tKODFHSEFCUjBZJmVuY3J5cHRlZElkPUExMDQ1MjQ0M09PQ0RSWDE0QjBSSCZlbmNyeXB0ZWRBZElkPUEwMTE1MTI1M002NjJPRkpJWFRSTiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

page= requests.get(URL,headers=headers)

soup=bs(page.content, "html.parser")

sender= 'amazonPriceTracker1010@gmail.com'
password='avhbkcuorkvhhyzb'

def price_checker():
    title = soup.find(id='productTitle').get_text()
    price= soup.find(id='priceblock_ourprice').get_text()
    clean_price= price[3:8]
    print(title)
    if clean_price < 130:
    send_mail()


def send_mail(sender,password,receiver='fadelnasereddin6@gmail.com'):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)

    subject= "Yo man I found a Great Deal for you!"
    body= "This is is the link for the discounted product: \n 'https://www.amazon.ca/Keurig-K-Select-Coffee-Maker-Matte/dp/B07B8SQXLK/ref=sr_1_1_sspa?crid=3M68BKCL5AGLC&keywords=keurig+coffee+maker&qid=1584239335&sprefix=keurgi%2Caps%2C272&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0tKODFHSEFCUjBZJmVuY3J5cHRlZElkPUExMDQ1MjQ0M09PQ0RSWDE0QjBSSCZlbmNyeXB0ZWRBZElkPUEwMTE1MTI1M002NjJPRkpJWFRSTiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='"
    message= f"Subject: {subject} \n \n {body}"

    server.sendmail(
        sender,
        receiver,
        message
    )
    print('MESSAGE SENT SUCCESSFULLY')

    server.quit()

while(True):
    price_checker()
    time.sleep(60*120)
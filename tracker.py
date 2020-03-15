import requests #Accesses URL
from bs4 import BeautifulSoup as bs 
import smtplib
import time 

## Declaring variables for desired page we wish to pull from ## 
URL='https://www.amazon.ca/Keurig-K-Select-Coffee-Maker-Matte/dp/B07B8SQXLK/ref=sr_1_1_sspa?crid=3M68BKCL5AGLC&keywords=keurig+coffee+maker&qid=1584239335&sprefix=keurgi%2Caps%2C272&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT0tKODFHSEFCUjBZJmVuY3J5cHRlZElkPUExMDQ1MjQ0M09PQ0RSWDE0QjBSSCZlbmNyeXB0ZWRBZElkPUEwMTE1MTI1M002NjJPRkpJWFRSTiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
page= requests.get(URL,headers=headers)
soup=bs(page.content, "html.parser")

## Declaring variables of sender, receiver, and password to access account and send email ##
sender= 'amazonPriceTracker1010@gmail.com'
password='avhbkcuorkvhhyzb'
receiver='fadelnasereddin6@gmail.com'

## Scraping Title & Price of item from URL ##
title = soup.find(id='productTitle').get_text()
price= soup.find(id='priceblock_ourprice').get_text()
clean_price= float(price[4:8])
clean_title= title.strip()

def price_checker():
    if clean_price < 130:
        send_mail(sender,password,receiver)


def send_mail(sender,password,receiver):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender,password)

    subject= f"Yo Steph I found a Great Deal for you on this item: {clean_title} "
    body= f"This is is the link for the discounted product: {URL}"
    message= f"Subject: {subject}\n\n{body}"

    server.sendmail(
        sender,
        receiver,
        message
    )
    print('MESSAGE SENT SUCCESSFULLY')

    server.quit()

while(True):
    price_checker()
    print("Will commence re-checking after 2 hours.")
    time.sleep(60*120)
import requests
import re
import time
from lxml import html
from lxml import etree
import sched, time

def Scrape(multId):
    card_page = requests.get(f'https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid={multId}')
    tree = html.fromstring(card_page.content)

    card_details = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol"]/div[2]/node()')

    try:
      mana_symbol = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow"]/div[2]/img')
      print(mana_symbol[0].get('alt'))
    except:
      print('No mana symbol or incorrect path')

    try:
      tap_symbol = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow"]/div[2]/div/img')
      print(tap_symbol[0].get('alt'))
    except:
      print('No beginning of text symbol or incorrect path')


    # /src() in the place of node() above may prove useful
    # /alt() as well assuming it exists... 

    temp = ''
    for i in range(len(card_details)):
        if(str(card_details[i]).find('Element') != -1):
          temp += Format(card_details[i].text_content()) + '\n'
    
    tempList = temp.split('\n')

    for i in range(len(tempList)):
        print(tempList[i])
 
    f = open('text.txt', 'ab+')
    f.write(temp.encode('utf8'))
    f.close()

def Format(str):
    return re.sub(' +',' ',str.strip().replace('\r\n',''))

# for i in range(1,10):
#   Scrape(i)
#   time.sleep(.5)

Scrape(345)
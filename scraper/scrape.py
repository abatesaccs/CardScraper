import requests
import re
import time
from lxml import html
from lxml import etree
import sched, time

def Scrape(multId):
    card_page = requests.get(f'https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid={multId}')
    tree = html.fromstring(card_page.content)

    try:
      card_details = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol"]/div[2]/node()')
    except:
      print('card path is incorrect')

    # /src() in the place of node() above may prove useful

    try:
      mana_symbol = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow"]/div[2]/img')
      num_icons = len(mana_symbol)
      mana_cost = ' '
      for i in range(num_icons):
        mana_cost += mana_symbol[i].get('alt')
        if(i != num_icons - 1):
          mana_cost += ', '
      print(mana_cost)
    except:
      print('No mana symbol or incorrect path')

    try:
      tap_symbol = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow"]/div[2]/div/img')
      print(tap_symbol[0].get('alt'))
    except:
      print('No beginning of text symbol or incorrect path')

    temp = ''
    for i in range(len(card_details)):
        if(str(card_details[i]).find('Element') != -1):
          if('Mana Cost' in card_details[i].text_content() and not ('Converted' in card_details[i].text_content())):
            temp += Format(card_details[i].text_content()) + mana_cost + '\n'
          else:
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

Scrape(378436)
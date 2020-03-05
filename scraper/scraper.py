import requests
import re
from lxml import html
from lxml import etree
import sched, time

def Scrape():
    card_page = requests.get('https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=3')
    tree = html.fromstring(card_page.content)

    card_details = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol"]/div[2]/node()')

    temp = ''
    for i in range(len(card_details)):
        if(str(card_details[i]).find('Element') != -1):
            temp += Format(card_details[i].text_content()) + '\n'
    
    tempList = temp.split('\n')

    for i in range(len(tempList)):
        print(tempList[i])
 
    f = open('text.txt', 'a+')
    f.write(temp.encode('utf8'))
    f.close()

def Format(str):
    return re.sub(' +',' ',str.strip().replace('\r\n',''))

Scrape() 
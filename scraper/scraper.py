import requests
import re
from lxml import html
from lxml import etree
import sched, time

def Scrape():
    card_page = requests.get('https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=416938')
    tree = html.fromstring(card_page.content)

    card_details = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol"]/div[2]')

    temp = ''
    for i in range(len(card_details)):
        if(str(card_details[i]).find('Element') != -1):
            temp += card_details[i].text_content()

    tempText = Format(temp)
    print(tempText)

    f = open('text.txt', 'w+')
    f.write(tempText.encode('utf8'))
    f.close()

def Format(str):
    return re.sub(' +',' ',str.strip().replace('\r\n',''))

Scrape()

# formatted = title[0].strip()
# print(tree)
# print(small_grey)
# print(title[0])
# print(title)
# print(formatted)
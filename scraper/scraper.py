import requests
import re
from lxml import html
from lxml import etree
import sched, time

def Scrape():
    card_page = requests.get('https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=416938')
    tree = html.fromstring(card_page.content)

    small_grey = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol"]/div[2]')

    temp = ''
    for i in range(len(small_grey)):
        if(str(small_grey[i]).find('Element') != -1):
            temp += small_grey[i].text_content()

    # tempText = ''
    # for i in range(len(temp)):
    #     tempText += temp[i].text_content().strip() + '|||'
    # tempText = tempText.replace('\r\n', '')
    # tempText = re.sub(' +',' ',tempText)
    tempText = Format(temp)
    print(tempText)

def Format(str):
    return re.sub(' +',' ',str.strip().replace('\r\n',''))

Scrape()

# formatted = title[0].strip()
# print(tree)
# print(small_grey)
# print(title[0])
# print(title)
# print(formatted)
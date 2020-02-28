import requests
import re
from lxml import html
from lxml import etree
import sched, time

def Scrape():
    card_page = requests.get('https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=416938')
    tree = html.fromstring(card_page.content)

    card_details = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol"]/div[2]/node()')

    print(len(card_details))

    temp = ''
    
    # temp = Format(card_details[7].text_content())
    for i in range(len(card_details)):
        if(str(card_details[i]).find('Element') != -1):
            temp += Format(card_details[i].text_content()) + '\n'
    
    tempList = temp.split('\n')
    # tempList = tempList.remove(u'')
    print(temp + '\n\n\n')
    print(tempList)

    for i in range(len(tempList)):
        print(tempList[i])
 
    # f = open('text.txt', 'w+')
    # f.write(tempText.encode('utf8'))
    # f.close()

def Format(str):
    return re.sub(' +',' ',str.strip().replace('\r\n',''))

Scrape()

# formatted = title[0].strip()
# print(tree)
# print(small_grey)
# print(title[0])
# print(title)
# print(formatted)
import requests
from lxml import html

card_page = requests.get('https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=416938')
tree = html.fromstring(card_page.content)

title = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_nameRow"]/div[2]/text()')
cmc = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cmcRow"]/div[2]/text()')

formatted = title[0].strip()

print(title)
print(cmc)
print(title[0])
print(formatted)
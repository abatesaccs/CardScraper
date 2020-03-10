import requests
import re
import time
import sqlite3
import json
from lxml import html
from lxml import etree
from card import *
import sched, time


def Scrape(multId, numCards):
  # connection = sqlite3.connect('cardTable.db')
  connection = sqlite3.connect(':memory:')
  c = connection.cursor()

  with connection:
    c.execute("""CREATE TABLE IF NOT EXISTS cards (
        cardId integer,
        name text,
        manaCost text,
        convertedManaCost integer,
        type text,
        body text,
        flavor text,
        expansion text,
        rarity text,
        sets text,
        number integer,
        artist text
        )""")
  
  for x in range(numCards):
    multId += x
    card_page = requests.get(f'https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid={multId}')
    tree = html.fromstring(card_page.content)
    card_dict = {
      'Multiverse Id': multId
    }

    try:
      card_details = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rightCol"]/div[2]/node()')
    except:
      print('card path is incorrect')

    try:
      mana_symbol = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow"]/div[2]/img')
      num_icons = len(mana_symbol)
      mana_cost = ' '
      for i in range(num_icons):
        mana_cost += mana_symbol[i].get('alt')
        if(i != num_icons - 1):
          mana_cost += ', '
    except:
      print('No mana symbol or incorrect path')

    try:
      tap_symbol = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow"]/div[2]/div/img')
      num_icons = len(tap_symbol)
      body_symbol = ' '
      for i in range(num_icons):
        body_symbol += tap_symbol[i].get('alt')
        if(i != num_icons - 1):
          body_symbol += ', '
    except:
      print('No beginning of text symbol or incorrect path')

    try:
      sets_symbol = tree.xpath('//*[@id="ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_otherSetsValue"]/div/a/img')
      num_icons = len(sets_symbol)
      set_text_list = ' '
      for i in range(num_icons):
        set_text_list += sets_symbol[i].get('alt')
        if(i != num_icons - 1):
          set_text_list += ', '
    except:
      print('No only one set or incorrect path')

    # Use label and value classes in elements to separate key and value for use in Card class

    temp_string = ''
    temp_item = ''
    for i in range(len(card_details)):
        if(str(card_details[i]).find('Element') != -1):
          if('Mana Cost' in card_details[i].text_content() and not ('Converted' in card_details[i].text_content())):
            temp_string += formatted(card_details[i].text_content()) + mana_cost + '\n'
            temp_item = formatted(card_details[i][0].text_content())
            card_dict[keyFormat(temp_item)] = mana_cost
          # elif(num_icons > 0):
          #   textbox = tree.find_class('cardtextbox')
          #   for j in range(len(textbox)):
          #     if(card_details[i] == textbox):
          #       print('in deep loop')
          elif('All Sets' in card_details[i].text_content()):
            temp_string += formatted(card_details[i].text_content()) + set_text_list + '\n'
            temp_item = formatted(card_details[i][0].text_content())
            card_dict[keyFormat(temp_item)] = set_text_list
          else:
            temp_string += formatted(card_details[i].text_content()) + '\n'
            temp_item = formatted(card_details[i][0].text_content())
            try:
              card_dict[keyFormat(temp_item)] = formatted(card_details[i][1].text_content())
            except:
              continue
    
    my_card = Card(card_dict)
    my_card.populate()

    table_columns = []
    table_values = []
    for i in card_dict:
      if(i == 'Multiverse Id'):
        table_columns.append("cardId")
        table_values.append(card_dict[i])
      elif(i == 'Card Name'):
        table_columns.append("name")
        table_values.append(card_dict[i])
      elif(i == 'Mana Cost'):
        table_columns.append("manaCost")
        table_values.append(card_dict[i])
      elif(i == 'Converted Mana Cost'):
        table_columns.append("convertedManaCost")
        table_values.append(card_dict[i])
      elif(i == 'Type'):
        table_columns.append("type")
        table_values.append(card_dict[i])
      elif(i == 'Card Text'):
        table_columns.append("body")
        table_values.append(card_dict[i])
      elif(i == 'Flavor Text'):
        table_columns.append("flavor")
        table_values.append(card_dict[i])
      elif(i == 'Expansion'):
        table_columns.append("expansion")
        table_values.append(card_dict[i])
      elif(i == 'Rarity'):
        table_columns.append("rarity")
        table_values.append(card_dict[i])
      elif(i == 'All Sets'):
        table_columns.append("sets")
        table_values.append(card_dict[i])
      elif(i == 'Card Number'):
        table_columns.append("number")
        table_values.append(card_dict[i])
      elif(i == 'Artist'):
        table_columns.append("artist")
        table_values.append(card_dict[i])

    for i in range(len(table_columns)):
      with connection:
        if(i == 0):
          c.execute(f"INSERT INTO cards ({json.dumps(table_columns[i])}) VALUES ({table_values[i]})")
        else:
          c.execute(f'UPDATE cards SET {json.dumps(table_columns[i])} = ? WHERE cardId = {table_values[0]}',(table_values[i],))

    c.execute('SELECT * FROM cards')
    print(c.fetchall())

    tempList = temp_string.split('\n')

    for i in range(len(tempList)):
        print(tempList[i])
 
    f = open('text.txt', 'ab+')
    f.write(temp_string.encode('utf8'))
    f.close()
    time.sleep(.5)
  connection.close()

def formatted(str):
  return re.sub(' +',' ',str.strip().replace('\r\n',''))

def keyFormat(str):
  return re.sub(':', '', str.strip())



# Scrape(247173) middle of the text
# Scrape(10704) multiple sections

class Card:
  
  def __init__(self, card_data):
    self.card_data = card_data
    self.card_id = 0
    self.name = ''
    self.mana_cost = ''
    self.converted_mana_cost = 0
    self.type = ''
    self.body = ''
    self.flavor = ''
    self.expansion = ''
    self.rarity = ''
    self.sets = ''
    self.number = 0
    self.artist = ''

  def populate(self):
    for i in self.card_data:
      if(i == 'Multiverse Id'):
        self.card_id = self.card_data[i]
      elif(i == 'Card Name'):
        self.name = self.card_data[i]
      elif(i == 'Mana Cost'):
        self.mana_cost = self.card_data[i]
      elif(i == 'Converted Mana Cost'):
        self.converted_mana_cost = self.card_data[i]
      elif(i == 'Type'):
        self.type = self.card_data[i]
      elif(i == 'Card Text'):
        self.body = self.card_data[i]
      elif(i == 'Flavor Text'):
        self.flavor = self.card_data[i]
      elif(i == 'Expansion'):
        self.expansion = self.card_data[i]
      elif(i == 'Rarity'):
        self.rarity = self.card_data[i]
      elif(i == 'All Sets'):
        self.sets = self.card_data[i]
      elif(i == 'Card Number'):
        self.number = self.card_data[i]
      elif(i == 'Artist'):
        self.artist = self.card_data[i]

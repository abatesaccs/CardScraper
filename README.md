# MTGCardScraper

Andrew Bates

## Project Description

### Goal

This project will allow users to scrape Magic the Gathering card data from Gatherer.Wizards.com based on specific search criteria

### Example card data

Card Name: Black Lotus  
Mana Cost:  
Converted Mana Cost: 0  
Types: Artifact  
Card Text: , Sacrifice Black Lotus: Add three mana of any one color.  
Expansion: Limited Edition Alpha  
Rarity: Rare  
All Sets:  
Artist: Christopher Rush  
_This is currently missing card and icon images_

### MVP

The ability to return a single cards data from Gatherer  
Store the returned cards data in a database  
Return card data from the database  

### Tools currently being used

Python  
[lxml](https://lxml.de/)  
[Requests](https://requests.readthedocs.io/en/master/)  
[SQLite](https://www.sqlite.org/index.html)

### Big Dreams

Retrieve card based on various search criteria e.g.  Color, Type, Name, P/T etc.  
Retrieve multiple cards based on search criteria  
Retrieve card images  
Create an API to return the information in the database  
Create a site to host and document the api  

### Potential resources

AWS Database  
SQLAlchemy  
AWS Lambda  
AWS T2  
A Domain  
Swagger  

### Potential Schema Structure

        CardId
        Card Name
        Mana Cost - optional
        Converted Mana Cost - optional
        Card Type
        Card Text
        Flavor - optional
        Expansion
        Rarity
        Sets - optional
        Number
        Artist

### Potential API endpoints

        Search/MultId/{id}
        Search/Name/{name}

### Classes 

        Scrape() - Scrape the site for the card data
        Format() - Format the card data; clean up the rough edges
        Save() - Add the card to database

### Current task

Find the values of card symbols and replace current blanks with appropriate text  

Notes:    
If there is only one result from a search it returns the cards page, if there are multiple results it returns a list of links to each card  
The differences between search and card urls are such:  

        Search/Default.aspx?name=+[rat]
        Card/Details.aspx?multiverseid=29857  

_note, this is the first card returned called acceleRATe, the serch is very accepting_
 
Multiple words in a search are shown as:

        Search/Default.aspx?name=+[bog]+[r]

Additionally, the search 'bog rat' and 'bog rats' both return the url:  

        Card/Details.aspx?multiverseid=2798

Which is the card page for bog rats, if the search can only return one card even if the term is incomplete, it will return the card page  
 
Even more impressive is that if you search for 'bog cat' it returns

        Card/Details.aspx?multiverseid=139471

Which is the card 'Caterwauling Boggart', if the search can fit into a card regardless of order, it will return the card 


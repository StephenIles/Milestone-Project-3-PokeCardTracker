from flask import Flask, render_template, request, redirect, url_for
from pokecollector import app, db
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity


@app.route("/")
def home():
    cards = Card.where(page=1, pageSize=30)
    sets = Set.where(page=1, pageSize=6)
    return render_template("index.html", cards=cards, sets=sets)

@app.route("/set_search")
def set_search():
    sets = Set.all()
    series = []
    for set in sets:
        if set.series not in series:
            series.append(set.series)
    return render_template("set_search.html", sets=sets, series=series)

@app.route("/card_search")
def card_search():
    return render_template("card_search.html")

@app.route("/sets/<sets_id>")
def sets(sets_id):
    sets = Set.where(q=f'id:"{sets_id}"')
    cards = Card.where(q=f'set.id:"{sets_id}"')
    return render_template("set_page.html", sets=sets, cards=cards)

@app.route("/cards/<card_id>")
def cards(card_id):
    card = Card.where(q=f'id:"{card_id}"')
    subtypes = Subtype.all()
    type_url = None
    attacks_urls = []
    
    # checks for pokemon types and assigns the correct image
    match card[0].types:
        case ['Water']:
            type_url = 'img/water.png'
        case ['Colorless']:
            type_url = 'img/colorless.png'
        case ['Darkness']:
            type_url = 'img/darkness.png'
        case ['Dragon']:
            type_url = 'img/dragon.png'
        case ['Fairy']:
            type_url = 'img/fairy.png'
        case ['Fighting']:
            type_url = 'img/fighting.png'
        case ['Fire']:
            type_url = 'img/fire.png'
        case ['Grass']:
            type_url = 'img/grass.png'
        case ['Lightning']:
            type_url = 'img/lightning.png'
        case ['Metal']:
            type_url = 'img/metal.png'
        case ['Psychic']:
            type_url = 'img/psychic.png'
            
            
    # checks for attack type, adding images for each attck cost.        
    for attack in card[0].attacks:
        for each in attack.cost:
            attack_cost_urls = []
            match each:
                case 'Water':
                    attack_cost_urls.append('img/water.png')
                case 'Colorless':
                    attack_cost_urls.append('img/colorless.png')
                case 'Darkness':
                    attack_cost_urls.append('img/darkness.png')
                case 'Dragon':
                    attack_cost_urls.append('img/dragon.png')
                case 'Fairy':
                    attack_cost_urls.append('img/fairy.png')
                case 'Fighting':
                    attack_cost_urls.append('img/fighting.png')
                case 'Fire':
                    attack_cost_urls.append('img/fire.png')
                case 'Grass':
                    attack_cost_urls.append('img/grass.png')
                case 'Lightning':
                    attack_cost_urls.append('img/lightning.png')
                case 'Metal':
                    attack_cost_urls.append('img/metal.png')
                case 'Psychic':
                    attack_cost_urls.append('img/psychic.png')
            attacks_urls.append(', '.join(attack_cost_urls))  # converts list to string.      
                
            
    return render_template("card_page.html", card=card, subtypes=subtypes, type_url=type_url, attacks_urls=attacks_urls)
    
    
from flask import render_template, request, redirect, url_for
from pokecollector import app, db
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

@app.route("/")
def home():
    cards = Card.where(q='name:charizard')
    return render_template("index.html", cards=cards)
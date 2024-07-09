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

@app.route("/sets/<sets_name>")
def sets(sets_name):
    sets = Set.all()
    for set in sets:
        if set.name == sets_name:
            active_set = sets_name
    cards = Card.where(q='set.name=<sets_name>')
    return render_template("set_page.html", active_set=active_set, sets=sets, cards=cards)
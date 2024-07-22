from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
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
    weakness_urls = []
    retreat_urls = []
    
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
        
    # check the weakeness type and assigns the correct url
    if card[0].weaknesses != None:   
        for weakness in card[0].weaknesses:
            each_weakness_urls = []
            match weakness.type:
                case 'Water':
                    each_weakness_urls.append('img/water.png')
                case 'Colorless':
                    each_weakness_urls.append('img/colorless.png')
                case 'Darkness':
                    each_weakness_urls.append('img/darkness.png')
                case 'Dragon':
                    each_weakness_urls.append('img/dragon.png')
                case 'Fairy':
                    each_weakness_urls.append('img/fairy.png')
                case 'Fighting':
                    each_weakness_urls.append('img/fighting.png')
                case 'Fire':
                    each_weakness_urls.append('img/fire.png')
                case 'Grass':
                    each_weakness_urls.append('img/grass.png')
                case 'Lightning':
                    each_weakness_urls.append('img/lightning.png')
                case 'Metal':
                    each_weakness_urls.append('img/metal.png')
                case 'Psychic':
                    each_weakness_urls.append('img/psychic.png')
            weakness_urls.append(', '.join(each_weakness_urls))  # converts list to string.
            
    # checks the retreat cost and assigns the correct urls
    for retreat in card[0].retreatCost:
        each_retreat_urls = []
        match retreat:
            case 'Water':
                each_retreat_urls.append('img/water.png')
            case 'Colorless':
                each_retreat_urls.append('img/colorless.png')
            case 'Darkness':
                each_retreat_urls.append('img/darkness.png')
            case 'Dragon':
                each_retreat_urls.append('img/dragon.png')
            case 'Fairy':
                each_retreat_urls.append('img/fairy.png')
            case 'Fighting':
                each_retreat_urls.append('img/fighting.png')
            case 'Fire':
                each_retreat_urls.append('img/fire.png')
            case 'Grass':
                each_retreat_urls.append('img/grass.png')
            case 'Lightning':
                each_retreat_urls.append('img/lightning.png')
            case 'Metal':
                each_retreat_urls.append('img/metal.png')
            case 'Psychic':
                each_retreat_urls.append('img/psychic.png')
        retreat_urls.append(', '.join(each_retreat_urls))  # converts list to string.      
                
            
    return render_template("card_page.html", card=card, subtypes=subtypes, type_url=type_url, attacks_urls=attacks_urls, weakness_urls=weakness_urls, retreat_urls=retreat_urls)

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=['POST'])
def signup_post():
    #code to validate and add user to database
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    # check to see if email is already in the database
    user = User.query.filter_by(email=email).first()
    
    # if the user is found will redirect to user signup page
    if user:
        flash('Email address already exists')
        return redirect(url_for("signup"))
    
    # create a new user with the form data. Hash the password so the plaintext version isn't saved
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
    
    # add the new user to the datadase
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for("login"))

@app.route("/login", methods=['POST'])
def login_post():
    # login code
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False
    
    user = User.query.filter_by(email=email).first()
    
    # check if the user actually exisits
    # takes the user supplied password, hash it and compares it to the stored password for this email.
    if not user or not check_password_hash(user.password, password):
        flash('Please check your user login details and try again.')
        return redirect(url_for('login')) # if the user doesn't ewxists or the password in incorrect will take them back to the login page.
    
    # if they pass all checks and login in take them to their user page.
    return redirect(url_for("account"))
    
    
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, UserCards
from flask_login import login_user, current_user, login_required, logout_user
from pokecollector import app, db
from pokemontcgsdk import Card, Set, Type, Supertype, Subtype, Rarity
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG)


@app.route("/")
def home():
    logging.debug("Home page accessed")
    cards = Card.where(page=1, pageSize=30)
    sets = Set.where(page=1, pageSize=6)
    logging.debug(f"Fetched cards: {cards}")
    logging.debug(f"Fetched sets: {sets}")
    return render_template("index.html", cards=cards, sets=sets)

@app.route("/set_search")
def set_search():
    logging.debug("Set search page accessed")
    sets = Set.all()
    series = []
    for set in sets:
        if set.series not in series:
            series.append(set.series)
    logging.debug(f"Fetched sets: {sets}")
    logging.debug(f"Series list: {series}")
    return render_template("set_search.html", sets=sets, series=series)

@app.route('/card_search_post', methods=['POST'])
def card_search_post():
    logging.debug("Card search post route accessed")
    search_query = request.form.get("search")
    logging.debug(f"Search query: {search_query}")
    # Redirect to the GET route with the search query in the URL
    return redirect(url_for('card_search', search=search_query))

@app.route('/card_search', methods=['GET'])
def card_search():
    logging.debug("Card search page accessed")
    # Get the search query from the URL parameters
    search_query = request.args.get('search', '')
    cards = Card.where(q=f'name:"{search_query}"') if search_query else []
    logging.debug(f"Search query: {search_query}")
    logging.debug(f"Fetched cards: {cards}")
    return render_template('card_search.html', cards=cards)
    

@app.route("/sets/<sets_id>")
def sets(sets_id):
    logging.debug("Set page accessed")
    sets = Set.where(q=f'id:"{sets_id}"')
    cards = Card.where(q=f'set.id:"{sets_id}"')
    logging.debug(f"Fetched set: {sets}")
    return render_template("set_page.html", sets=sets, cards=cards)

@app.route("/cards/<card_id>")
def cards(card_id):
    logging.debug("Card page accessed")
    card = Card.where(q=f'id:"{card_id}"')
    subtypes = Subtype.all()
    type_url = None
    attacks_urls = []
    weakness_urls = []
    retreat_urls = []
    
    # checks for pokemon types and assigns the correct image
    if card[0].types != None:
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
    if card[0].attacks != None:
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
    if card[0].retreatCost != None:
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

    # debug logging
    logging.debug(f"Card: {card}")
    logging.debug(f"Subtypes: {subtypes}")
    logging.debug(f"Type URL: {type_url}")
    logging.debug(f"Attacks URLs: {attacks_urls}")
    logging.debug(f"Weakness URLs: {weakness_urls}")
    logging.debug(f"Retreat URLs: {retreat_urls}")
    logging.debug(f"Card ID: {card_id}")
                 
    return render_template("card_page.html", card=card, subtypes=subtypes, type_url=type_url, attacks_urls=attacks_urls, weakness_urls=weakness_urls, retreat_urls=retreat_urls)

@app.route("/signup")
def signup():
    logging.debug("Signup page accessed")
    return render_template("signup.html")

@app.route("/login")
def login():
    logging.debug("Login page accessed")
    return render_template("login.html")

@app.route("/profile")
@login_required
def profile():
    logging.debug("Profile page accessed")
    sets = Set.all()
    series = []
    for set in sets:
        if set.series not in series:
            series.append(set.series)
    user_cards = UserCards.query.filter_by(user_id=current_user.id).all()

    # Sort user cards by card number
    user_cards_sorted = sorted(user_cards, key=lambda uc: uc.card_number)

    user_cards_dict = {uc for uc in user_cards_sorted}

    # debug logging
    logging.debug(f"Sets: {sets}")
    logging.debug(f"Series: {series}")
    logging.debug(f"User cards: {user_cards}")
    logging.debug(f"User cards sorted: {user_cards_sorted}")
    logging.debug(f"User cards dict: {user_cards_dict}")
    logging.debug(f"Current user: {current_user}")

    return render_template("account.html", name=current_user.name, sets=sets, series=series, user_cards_dict=user_cards_sorted)

@app.route('/logout')
@login_required
def logout():
    logging.debug("User logged out")
    logout_user()
    return redirect(url_for('home'))

@app.route("/signup", methods=['POST'])
def signup_post():
    logging.debug("Signup post route accessed")
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

    # debug logging
    logging.debug(f"New user: {new_user}")
    logging.debug(f"User added to database")
    
    return redirect(url_for("login"))

@app.route("/login", methods=['POST'])
def login_post():
    logging.debug("Login post route accessed")
    # login code
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False
    
    user = User.query.filter_by(email=email).first()
    
    # check if the user actually exisits
    # takes the user supplied password, hash it and compares it to the stored password for this email.
    if not user or not check_password_hash(user.password, password):
        flash('Please check your user login details and try again.')
        return redirect(url_for('login')) # if the user doesn't exists or the password in incorrect will take them back to the login page.
    
    # if they pass all checks and login in take them to their user page.
    login_user(user, remember=remember)
    logging.debug(f"User logged in: {user}")
    return redirect(url_for("profile"))
    
@app.route("/add_collection/<card_id>", methods=['POST'])
@login_required
def add_collection(card_id):
    logging.debug("Add collection route accessed")
    # Pull the corresponding card information
    card = Card.where(q=f'id:"{card_id}"')
    
    if not card:
        return redirect(url_for('home'))  # Redirect to home or another route if card is not found

    card = card[0]  # Assuming `where` returns a list, get the first item

    # Pull user's cards
    user_cards = UserCards.query.filter_by(user_id=current_user.id).all()
    user_cards_dict = {uc.card_id for uc in user_cards}

    # Check if the user already has the card in the collection
    if card_id in user_cards_dict:
        logging.debug("Card already in user collection")
    else:
        # Build new card entry
        user_card_image = card.images.small  # Corrected image field access
        user_card_set = card.set.id  # Storing set ID instead of name (more precise)
        user_card_name = card.name
        user_card_number = card.number

        new_card = UserCards(
            user_id=current_user.id,
            card_id=card_id,
            card_image=user_card_image,
            set_id=user_card_set,
            card_name=user_card_name,
            card_number=user_card_number
        )

        # Commit new card to the database
        db.session.add(new_card)
        db.session.commit()

    # debug logging
    logging.debug(f"Card ID: {card_id}")
    logging.debug(f"Card: {card}")
    logging.debug(f"User cards: {user_cards}")
    logging.debug(f"User cards dict: {user_cards_dict}")
    logging.debug(f"New card: {new_card}")  
    logging.debug(f"Card added to user's collection")
    logging.debug(f"User: {current_user}")

    # Redirect back to the card's detail page
    return redirect(url_for('cards', card_id=card_id))

@app.route("/delete_user", methods=['POST'])
@login_required
def delete_user():
    # get the user record from the database
    user_id = current_user.id
    user = User.query.get(user_id)

    # if the user is in the database delete
    if user:
        db.session.delete(user)
        db.session.commit()
        logging.debug(f'User {user_id} deleted from database')
    # if not let the user know nothing was deleted
    else:
        logging.debug(f'User {user_id} not found in database')

    return redirect(url_for('home'))

@app.route("/delete_card/<card_id>", methods=["POST"])
@login_required
def delete_card(card_id):
    
    # Query the card to ensure it belongs to the current user
    card = UserCards.query.filter_by(card_id=card_id, user_id=current_user.id).first()

    if card:
        db.session.delete(card)
        db.session.commit()
        logging.debug(f'Card {card_id} deleted from user {current_user.id} collection')
    else:
        logging.debug(f'Card {card_id} not found in user {current_user.id} collection')

    # Redirect back to the card's detail page
    return redirect(url_for('cards', card_id=card_id))  



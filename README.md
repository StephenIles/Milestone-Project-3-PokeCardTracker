<h1 align="center">Milestone Project 3 - Pokemon Vault</h1>

## Live Website Link

[Pokemon Vault](https://pokemonvault-aa08546c246b.herokuapp.com/profile)

## Test User Login

**Email**: test123@test.com
**Password**: test123

## User Experience (UX)

- ### User stories

  - #### First Time Visitor Goals

    1. Crating an Account

       - Sign up: Click on the "Sign Up" button at the top right corner of the page.
       - Fill in Details: Provide your username, email and password.
       - Verify Email: Check your inbox for a verification email and follow the instructions.

    1. Explore the Card Database

       - Search for Cards: Use the serach bar to find specific cards by name.
       - View Card Details: Click on any card to see detailed information, including stats, rarity and pricing.

    1. Build Your Collection
       - Add Cards: Find the cards you own and add them to your personal collection.
       - Organize: Use filters and tags to organsize your collection by type, set or any other criteria.
       - Collection Goals: Add cards to your "To Get List" so you can easily find the inforamtion about these and keep up to date on the prices.

  - #### Frequent User Goals

    1. Expand and Update Your Collection

       - New Additions: Regulary add new cards to your collection as you aquire them.
       - Organize: Keep your collection organized using filters, tags, and catergories.
       - Showcase: Share and showcase your collection with friends and family.

    2. Set Long Term Goals
       - Complete Sets: Aim to complete entrie sets or special collections.
       - Collection Milestones: Set and achieve milestones for the number of cards, values, or specific themes.

- ### Design

  - #### Colour Scheme

    - The website features a minimalist colour scheme to ensure a clean and modern look. Predominantly, whites and greys are used to create a neutral background that allows the content to stand out. The default Materialize button colors are utilized for various buttons, providing a consistent and visually appealing interface. This simple yet effective colour scheme enhances readability and ensures that the focus remains on the content and functionality of the website.

  - #### Typography

    - - The website uses a clean and modern typography style to enhance readability and user experience. The primary font used is 'Roboto', which is known for its clarity and versatility. For headings and titles, 'Montserrat' is used to provide a distinct and elegant look. Both fonts are sourced from Google Fonts, ensuring they are web-safe and widely supported across different browsers and devices.

  - #### Imagery

    -The website utilizes high-quality imagery to enhance the visual appeal and user engagement. Images of the cards are prominently displayed to showcase their details and designs, providing users with a clear and attractive view of their collections. The use of consistent and relevant imagery helps to create a cohesive and immersive experience, making the website not only functional but also visually appealing. All images are optimized for fast loading times without compromising quality, ensuring a smooth and enjoyable user experience.

* ### Wireframes

  - Whole Website Wireframe - Wireframes for Mobile, Tablet and Web - [Wireframes](https://www.figma.com/design/f0PduV12NpOv423LKPF62q/Milestone-Project-3?node-id=44-912&t=5awXRw3JwP0VKP7n-1)

## Features

- Responsive on all device sizes

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

### Frameworks, Libraries & Programs Used

1. [Materialize CSS:](https://materializecss.com/getting-started.html)
   - Used for website layout and to help with the responsive deisgn of the website.
1. [Python](https://www.python.org)
   - Used to assist with API intergration
1. [Flask](https://flask.palletsprojects.com/en/3.0.x/)
   - Used to make the card and set pages from the database
1. [PostgreSQL](https://www.postgresql.org)
   - Used to store user collection information
1. [Heroku](https://id.heroku.com)
   - Used to host the website online
1. [Tembo](https://cloud.tembo.io)
   - Used to host the PostgerSQL Database
1. [Postman](https://web.postman.co)
   - Used to configure the API interaction.
1. [Google Fonts:](https://fonts.google.com/)
   - Used to import the fonts that were used
1. [Font Awesome:](https://fontawesome.com/)
   - Used for icons throughout the website.
1. [Javascript:](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
   - Used for some of the Materialize functionallity and thorughout the website
1. [Git](https://git-scm.com/)
   - Used for version control
1. [GitHub:](https://github.com/)
   - Used to host the repository
1. [Figma:](https://www.figma.com)
   - Used for wireframe and designing

## Testing

### Testing User Stories from User Experience (UX) Section

- #### First Time Visitor Goals

  1. **Creating an Account**

     - **Sign up**: Click on the "Sign Up" button at the top right corner of the page.
       - **Test**: Click the "Sign Up" button and verify that the sign-up form appears.
       - **Result**: The sign-up form appeared as expected.
       - **Status**: Pass
     - **Fill in Details**: Provide your username, email, and password.
       - **Test**: Fill in the sign-up form with a username, email, and password, then submit the form.
       - **Result**: The form was submitted successfully, and a verification email was sent.
       - **Status**: Pass

  2. **Explore the Card Database**

     - **Search for Cards**: Use the search bar to find specific cards by name.
       - **Test**: Enter a card name in the search bar and verify that the search results are displayed.
       - **Result**: The search results displayed the relevant cards.
       - **Status**: Pass
     - **View Card Details**: Click on any card to see detailed information, including stats, rarity, and pricing.
       - **Test**: Click on a card from the search results to view its details.
       - **Result**: The card details page displayed the correct information.
       - **Status**: Pass

  3. **Build Your Collection**
     - **Add Cards**: Find the cards you own and add them to your personal collection.
       - **Test**: Locate a card and add it to the personal collection.
       - **Result**: The card was successfully added to the personal collection.
       - **Status**: Pass

- #### Frequent User Goals

  1. **Expand and Update Your Collection**

     - **New Additions**: Regularly add new cards to your collection as you acquire them.
       - **Test**: Add a new card to the collection and verify that it appears correctly.
       - **Result**: The new card was added and displayed correctly in the collection.
       - **Status**: Pass

  2. **Set Long Term Goals**
     - **Complete Sets**: Aim to complete entire sets or special collections.
       - **Test**: Track progress towards completing a set and verify that the progress is accurately displayed.
       - **Result**: The progress towards completing the set was accurately tracked and displayed.
       - **Status**: Pass

### Further Testing

- The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
- A large amount of testing was done to ensure that all pages were linking correctly.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Testing Table

All aplication testing was done with logging statements throughout development. You can see these in the console when a page is loaded.

## Lighthouse Scores

The website was tested using Google Chrome's Lighthouse tool. Below are the scores:

### HomePage

- **Performance**: 72
- **Accessibility**: 77
- **Best Practices**: 71
- **SEO**: 91

### All Sets Page

- **Performance**: 93
- **Accessibility**: 77
- **Best Practises**: 79
- **SEO**: 91

### Set Pages

- **Performance**: 84
- **Accessibility**: 77
- **Best Practises**: 79
- **SEO**: 91

### Card Search (No Search)

- **Performance**: 100
- **Accessibility**: 80
- **Best Practises**: 79
- **SEO**: 91

### Card Search (With a search)#

- **Performance**: 70
- **Accessibility**: 80
- **Best Practises**: 75
- **SEO**: 91

### Profile

- **Performance**: 98
- **Accessibility**: 80
- **Best Practises**: 79
- **SEO**: 91

### Card Page

- **Performance**: 93
- **Accessibility**: 89
- **Best Practises**: 79
- **SEO**: 91

### Login Page

- **Performance**: 100
- **Accessibility**: 80
- **Best Practises**: 79
- **SEO**: 91

### Signup Page

- **Performance**: 100
- **Accessibility**: 80
- **Best Practises**: 79
- **SEO**: 91

There are performance issues due to the loading of images from the Pokemon API, a way around this may be been to clone to database to a local databse but in doing that I would not have the up to date inforamtion or would have to do a weekly update to make sure the data was correct.

### Known Bugs

Currently no known bugs that I havent been able to fix.

## Deployment

### Heroku

This project was deployed with Heroku. Follow these steps to deploy your project:

1. **Create an Account with Heroku**:

   - Go to [Heroku](https://www.heroku.com/) and sign up for a free account.

2. **Install the Heroku CLI**:

   - Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) for your operating system.

3. **Log in to Heroku via CLI**:

   ```bash
   heroku login
   ```

4. **Create a New Heroku App**:

   - Navigate to your project directory in the terminal.

   ```bash
   cd your-project-directory
   ```

   - Create a new Heroku app.

   ```bash
   heroku create your-app-name
   ```

5. **Link Your GitHub Repository**:

   - Go to the Heroku dashboard, select your app, and navigate to the "Deploy" tab.
   - Under "Deployment method", select "GitHub".
   - Connect to your GitHub account and search for your repository.
   - Click "Connect" to link your GitHub repository to the Heroku app.

6. **Set Up Environment Variables**:

   - In the Heroku dashboard, go to the "Settings" tab.
   - Click "Reveal Config Vars" and add the necessary environment variables. The variables you need to set up are:

     | Variable Name        | Description                                                    |
     | -------------------- | -------------------------------------------------------------- |
     | `DB_URL`             | The URL of your PostgreSQL database                            |
     | `SECRET_KEY`         | A secret key for your application                              |
     | `DEBUG`              | Set to `False` for production                                  |
     | `POKEMONTCG_API_KEY` | Get this key from [PokemonTCG API](https://dev.pokemontcg.io/) |
     | `IP`                 | The IP address to run the application                          |
     | `PORT`               | The port number to run the application                         |
     | `DEVELOPMENT`        | Set to `True` for development environments                     |

     Example:

     ```bash
     DB_URL=your-database-url
     SECRET_KEY=your-secret-key
     DEBUG=False
     POKEMONTCG_API_KEY=your-pokemontcg-api-key
     IP=0.0.0.0
     PORT=5000
     DEVELOPMENT=True
     ```

7. **Deploy the App**:

   - In the "Deploy" tab, under "Manual deploy", select the branch you want to deploy (usually `main` or `master`).
   - Click "Deploy Branch".

8. **Migrate the Database**:
   - Run the following commands to migrate the database:
   ```bash
   heroku run python manage.py migrate
   ```

### Database Hosting

1. **Tembo**:
   - Sign up for a free account at [Tembo](https://www.tembo.io/).
   - Create a new PostgreSQL database.
   - Copy the database URL provided by Tembo and add it to your Heroku config vars as `DATABASE_URL`.

### Forking the GitHub Repository

By forking the GitHub Repository, you make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository. Follow these steps:

1. **Log in to GitHub**:

   - Locate the [GitHub Repository](https://github.com/StephenIles/Milestone-Project-3-PokeCardTracker).

2. **Fork the Repository**:
   - At the top of the repository (not the top of the page), just above the "Settings" button on the menu, locate the "Fork" button.
   - Click "Fork" to create a copy of the repository in your GitHub account.

### Making a Local Clone

1. **Log in to GitHub**:

   - Locate the [GitHub Repository](https://github.com/StephenIles/Milestone-Project-3-PokeCardTracker).

2. **Clone the Repository**:

   - Under the repository name, click "Code" and then "Clone or download".
   - Copy the URL provided.
   - Open your terminal and run the following command:

   ```bash
   git clone https://github.com/StephenIles/Milestone-Project-3-PokeCardTracker
   ```

   - Navigate to the project directory:

   ```bash
   cd Milestone-Project-3-PokeCardTracker
   ```

3. **Install Dependencies**:

   - Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   - Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   - Create a `.env` file in the project root and add the necessary environment variables (e.g., `DATABASE_URL`, `SECRET_KEY`, etc.).

5. **Run the Application Locally**:
   - Apply migrations:
   ```bash
   python manage.py migrate
   ```
   - Run the development server:
   ```bash
   python manage.py runserver
   ```

By following these detailed instructions, you should be able to deploy your project on Heroku, set up the database, fork the repository, and make a local clone for development.

## Credits

### Code

### Content

- All content was written by the developer.

### Media

- All images where pulled throught the Pokemon

### Acknowledgements

- My Mentor for continuous helpful feedback.

## Problems and Soultions

### First Problem - Scrolling Cards

My first problem I came across was how to make the Pokemon cards scroll across the hero image section. I used some online resources looking at different ways to be able to accomplish this effect. I knew CSS animation was one way of doing it, but through my research I found an html tag for a marquee. I first implemented this tag and liked the effect but wanted to make a few changes to it.

```

  <div class="container hero-image valign-wrapper">
        <div class="row">
            <div class="col s12 marquee-container">
                <marquee behavior="scroll" direction="left">
                {% for card in cards %}
                    <img class="hero-card" src="{{ card.images.small }}">
                {% endfor %}
                </marquee>
            </div>
        </div>
    </div>

```

This is where I dug deeper to learn more about the marquee tag and this is then where I found that the tag had been depreicated and was no longer supported by more modern browsers. So finding this out I looked more into CSS animations and found I could replicate the effect I wanted. The following in the code I implemented and you will see in the project code.

```

    @keyframes marquee {
        from { transform: translateX(0%); }
        to   { transform: translateX(-100%); }
    }

    .marquee {
    animation: marquee 250s linear infinite;
    white-space: nowrap;
  }

```

### Second Problem - User Login

My second problem that I came across was creating the functionality for a user to be able to register, login and logout.
This was something new that I had never tried before but I knew it was going to be a important part of my project.

I did a lot of research online for this trying to figure out the best solution for a user system that would work well with the current tech stack. I did start by looking at [OAuth](https://auth0.com/) as this was a resource that I knew about and thought that it might work. While I was looking into how to intergrate OAuth into my current project I came across a Flask addon called [Flask Login](https://pypi.org/project/Flask-Login/) which gave me the functionallity that I was looking for without trying to learn a whole new system.

I figured this would be the best option for me to intergrate into the project as I am already using Flask.

I spent some time going through the Flask Login documentation and some online tutorials on youtube, to try and understand how Flask Login works.

### Third Problem - User Collection

My third problem came when I was building the user profile with the user collection. My initial thought for this was to make a check back for each available card with all cards being sorted into their own set groups. After attempting this the loading time for the profile page was way to long as it was checking every card against the criteria and would then eventually time out the connection meaning I needed to figure out a different way to go about setting up this profile.

My next idea was to add a card counter to each set title, displaying how many cards from that set that a user has marked that they have. Then to be able to add a card to their collection they would need to search for that specific card via either the card or the set search then on the card page click the add to collection button. Then if they want to remove a card from their collection they would need to untick the card of the profile page and press the save button to update their collection.

I feel like doing it this way gave users more control of making sure that they have selected the correct card, by checking all the inforamtion about the card while they are on the card page.

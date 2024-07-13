<h1 align="center">First Milestone Project 3 - Pokemon Vault</h1>

## Live Website Link

  [Pokemon Vault]()

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        

    -   #### Returning Visitor Goals

        

    -   #### Frequent User Goals
        

-   ### Design
    -   #### Colour Scheme
        -   
    -   #### Typography
        -   
    -   #### Imagery
        -   

*   ### Wireframes

    -   Whole Website Wireframe - Wireframes for Mobile, Tablet and Web - [Wireframes](https://www.figma.com/design/f0PduV12NpOv423LKPF62q/Milestone-Project-3?node-id=44-912&t=5awXRw3JwP0VKP7n-1)

## Features

-   Responsive on all device sizes

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

### Frameworks, Libraries & Programs Used

1. [Materialize CSS:](https://materializecss.com/getting-started.html)
1. [Python](https://www.python.org)
1. [Flask](https://flask.palletsprojects.com/en/3.0.x/)
1. [PostgreSQL](https://www.postgresql.org)
1. [Heroku](https://id.heroku.com)
1. [Tembo](https://cloud.tembo.io)
1. [Postman](https://web.postman.co)
1. [Google Fonts:](https://fonts.google.com/)
1. [Font Awesome:](https://fontawesome.com/)
1. [jQuery:](https://jquery.com/)
1. [Git](https://git-scm.com/)
1. [GitHub:](https://github.com/)
1. [Figma:](https://www.figma.com)

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input)

### Results


### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

      


-   #### Returning Visitor Goals

      

      
-   #### Frequent User Goals

      

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Testing Table




## Lighthouse Scores



### Known Bugs

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/StephenIles/OneLife-Milestone-Project-1-)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. In the menu on the left click on "Pages".
4. Under "Source", click the dropdown called "None" and select "main".
5. The page will automatically refresh.
6. Change the folder from "/root" to "/docs"
7. The page will automatically refresh
8. At the top of the page there will be a link to Visit the website.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/StephenIles/OneLife-Milestone-Project-1-)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/StephenIles/OneLife-Milestone-Project-1-)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code


### Content

-   All content was written by the developer.

### Media

-   All Images were created by the developer using [Dream Studio](https://beta.dreamstudio.ai/generate)

### Acknowledgements

-   My Mentor for continuous helpful feedback.

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
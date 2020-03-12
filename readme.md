# Pop World

For my Fourth and Final Milestone Project have chosen to build a project based on an auction website involving Pop!Vinyl's.  The goal of the website is for the Owner to advertise his Pop!Vinyl collection and sell them to the public involving either bidding for items or buying them out-right.

I will set up an authentication and authorisation.  Where only registered users can bid and buy items that are up for auction.

When the buyers come to purchase their goods, they will be using the Stripe Payment Method.

## Project Brief

- Earn money on selling the artifacts (the site owner is the seller)

- Create an online store focused on selling unique historical artifacts, such as The Holy Grail to the highest bidder.

- Allow users to search for artifacts based on various fields.

- Allow users to see the price, image and other basic details about an artifact.

- Users would be able to learn about the historical details of each artifact, the culture it came from, the way it was created and its journey across different owners in the past.

For example, you might want to include information about "events" that took place in the past and that one or more artifacts took place in, or originated from.

- Allow users to bid on items, or pay a higher price to purchase them immediately. Users have to be registered for this.

### Advanced potential feature (nice-to-have)

Allow registered users to write reviews about the artifacts, only if they purchased them.

Expand the search functionality to allow users to sort results based on price, age and other parameters in both ascending and descending order.

Include pagination and/or other dynamic display actions using javascript.

Use javascript polling to update the page whenever there's a new bid.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

| Technology      | How it was used                                                 | Website                                            |
| :--------------:|-----------------------------------------------------------------|---------------------------------------------------:|
| HTML            | Backbone of everything                                          | <https://www.w3schools.com/html/default.asp>         |
| CSS             | Styling for the MATERLIZE to work on                            | <https://www.w3schools.com/css/default.asp>          |
| MATERLIZE       | A modern responsive front-end framework based on Material Design| <https://materializecss.com/>                        |
| JAVASCRIPT      | Used for some functionality on the website                      | <https://www.w3schools.com/js/default.asp>           |
| PYTHON          | Used for the main functionality on the website                  | <https://www.w3schools.com/python/default.asp>       |
| SQLITE3         | Light Local Database                                | <https://www.sqlite.org/index.html>       |
| POST GRE           | Non-Relational Database                                         | <https://cloudmongo.com>                             |
| DJANGO          | Web Framework                                                    | <https://www.djangoproject.com/>|
| HEROKU          | Cloud Platform to Host the Django App                            | <https://id.heroku.com/login>                        |
| TRAVIS          | Testing Platform                                                 | <https://www.travis-ci.org/>                        |
| GITHUB          | Stores my work so that other people and myself can reference it | <https://www.github.com>                             |
| GITPOD          | An IDE allowing me to code on any browser                       | <https://www.gitpod.io>                              |
| VSCODE          | An IDE allowing me to code on my computer                       | <https://code.visualstudio.com/>                     |
| SLACK           | An chat application to allow others to communicate              | <https://slack.com/intl/en-gb/>                      |
| Stripe JS       | For easy payment when user select paynow option on all screen sizes | <https://stripe.com/ie>               |

## Places I Have Looked For Help

- Django Documentation - <https://docs.djangoproject.com/en/3.0/>

## Time-Line

### Saturday 7th March 2020

- Created readme.md file and populating with text.
- Created Django Project called "PopWorld"
- Created env.py file for Enviromental Variables
- Created .gitignore file to stop certain files being uploaded to GitHub
- Created Media folder for product images
- Created Static folder for js and css
- Created Root Templates folder for base.html
- Modifed settings.py in popworld folder, to use the Env.py settings and all the static files etc

### Monday 9th March 2020

- Copied Account App from previous tutorials, and integrate it into my project.
- Created Superuser.
- After copying over the accounts from, I am having issues with the Static files.  Going back to the course to refresh myself with the lessons on static files.
- Issue fixed, wasn't my static file settings.  I had 2 base.html and it was reading the wrong file.

- Test tried to create a new user, fails with the message "unable to log you in at this time!"
    However the user has been created in the admin menu.

- Test login user, fails with the message "your username or password are incorrect"

- Going back to the creating accounts videos on the Code Institute Website.

- After watching "Wiring Up The Authentication And Login" Video, I found out that the following code was missing from my views.py

- Test tried to create a new user, fails with the message "unable to log you in at this time!"
    However the user has been created in the admin menu. (Julie)

- Test tried to create a new user, fails with the message "unable to log you in at this time!"
    However the user has been created in the admin menu. (Barry)

- Test tried to create a new user, fails with the message "unable to log you in at this time!"
    However the user has been created in the admin menu. (Nate)

- Test tried to create a new user, fails with the message "unable to log you in at this time!"
    However the user has been created in the admin menu. (Nina)

- Test tried to create a new user, passes with the message "you have successfully registered"
    However the user has been created in the admin menu. (Vicki)

- Test tried to create a new user, passes with the message "you have successfully registered"
    However the user has been created in the admin menu. (Betty) and redirects to index.

### Tuesday 10th March 2020

- Test tried to reset password for a user, fails with a "connection refused". [Errno 61] Connection refused

- Added the ability to show an Email in the Console.  I may change this later if I can setup an smtp server, so I can send a proper email.

- Test tried to reset password for a user, passes with Output to the Console.

- Updated Base.html, and Custom.css, so it reflects more true to the project.

- Setup Testing for Django, once I have completed testing.  I will move onto the next part of the project.
    I have decided to come back to testing later, I need to get my project base down first.

- Watching "01 Testing Django" on the Code Institute Website.

- Using Coverage Reporting
    'coverage run manage.py test'
    'coverage report'
    'coverage run --source=accounts manage.py test'
    'coverage html'

- Created Home App

- Created Products App
    'makemigrate' --> my terminal shortcut for making migrations
    'migrate' --> my terminal shortcut for migrating

- Serving Error Fixed by Commenting out two lines.
    #from django.conf.urls.static import static
    #from django.contrib.staticfiles.urls import staticfiles_urlpatterns

- Added Extra Fields to the Models in Product, now have a migrating issue
    django.core.exceptions.ValidationError: ["'' value must be a decimal number."]

- Fixed Migrating Issue
    Thanks to Slack Users - Christos Gkoros & ckz8780 they had a conversation in regards to Christos migration error.  They talked about rolling back migrations and deleting unwanted migrations.
    'python3 manage.py showmigrations'
    then deleting the files in migrations and __pycache__ then re-migrating
    'makemigrate' --> my terminal shortcut for making migrations
    'migrate' --> my terminal shortcut for migrating

- Created New Product - Ichigo Kurosaki from the <https://www.popinabox.co.uk/merch-action-figures/bleach-ichigo-pop-vinyl-figure/11211524.html>

- It worked apart from I couldn't see the Image so I had to modify the CSS Code of the Product class.

### Wednesday 11th March 2020

- Created Auction App

    This is where the Auctions will be created and held.

    'makemigrate' --> my terminal shortcut for making migrations
    'migrate' --> my terminal shortcut for migrating

- Created Bids App

    This is where the Bids will be created and held within the Auctions.

    'makemigrate' --> my terminal shortcut for making migrations
    'migrate' --> my terminal shortcut for migrating

- Created Users App

    This is where Users will be created so that they can have access to the Auctions and make a bid.

    'makemigrate' --> my terminal shortcut for making migrations
    'migrate' --> my terminal shortcut for migrating

- Test - Tried to add a user in the user accounts, it failed stating that an integer was required instead of a string.  Maybe I should create a form where the id is inserted as an integer instead of going through the admin page?

- Test - Created User, however it wont create a copy in the User Profile Table.  Must be to do with the Views.py

- 6 Hours LATER,
    After repeated attempts at trying to link to models together and then wondering why I was getting
    "'User' object has no attribute 'UserProfile'"

    I deleted my database at least a dozen times while trying to get rid of all the test data I was sending to it.

    I did the only sane thing anyone would do and goto Youtube.
    <https://youtu.be/Tja4I_rgspI>

    Turns out I had created a users app, when I didn't need to so I deleted the app, and my database again.  Then followed through the Video.

- Test - Created User, PASSED :-)

- Updated Profile page, after struggling with the form.  I thought I would complete the profile page for users.

- Need to design a way for Owner to Add Products
    base.html - modified.

### Thursday 12th March 2020

- Another 6 Hours later, I have managed to allow the owner to add products.
    But they cant at the moment have images,
    And there are duplicates.

- Messed up my Migrations file so I'm going to start again, from the beginning.

### STARTED PROJECT AGAIN

I have used some code from my old project found here at <https://github.com/jjackson19862017/PopWorld>
To save time I will use code from previous attempt, however will do everything from scratch.

- 30 Minutes Later
    I have got back to where I want with my Project.

- Test - Add Product from Admin section, works with the image.
- Test - Add Product from form post, fails.
    Im still thinking that its the form/model ????
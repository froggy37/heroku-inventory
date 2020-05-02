# Heroku-Inventory

Very Simple Flask Server to be deploy in heroku platform as a means of web services testing

# Structure

- inventory.py => simple flask server
- inventory.json => json file containing list of network interfaces composing a dummy inventory
- Procfile => Heroku configuration to tell heroku how to start the application

# Instructions

https://devcenter.heroku.com/articles/heroku-cli

- Install Heroku Cli (mac)
```
brew tap heroku/brew && brew install heroku
```
- Login
```
heroku login
```

Before login make sure you create an account in heroku

https://dashboard.heroku.com/

- Create application
```
heroku create test-inventory-37
```

This will also instantiate a new git remote repository to which you push your codebase to have heroku instantiate the flask server

git push https://git.heroku.com/test-inventory-37.git


Then you can connect using any browser at:

https://test-inventory-37.herokuapp.com/
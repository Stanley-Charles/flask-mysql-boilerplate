# SportsBettr Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## About SportsBettr
Hello! Welcome to SportsBettr, founded by Stanley Charles, Akash Alaparthi and Arnav Sawant! We are 3 people who have taken an active interest in the Sports Betting Industry. Through our expirience, we have found that there has been an infux of "experts" in the Sports Betting Industry who's job it is to study odds, teams and outcomes, and to give their "take" on a certain bet(s). However, we have found that there is no centralized place for the everyday person (such as ourselves) to find and connect with these experts. This is why we created SportsBettr, to allow the everyday person to connect and hear directly from a Sports Betting expert (Our "Verified Users") in order to place better bets themselves. 

## Overview of Project
### Phase 1
During phase 1 we created 3 distinct User Personas. The first persona is a Verified User, who is one of the "experts" mentioned above. A Verified User can create "Posts" about a specific game and their "take" on that game. Their take can just be a comment about how they feel about Spread Odds, Team Prop(s), or Player Props. The second Persona is a Normal User. This is the everyday person mentioned above. This user is able to view any posts by verified users and can have a reaction on them (like, dislike, comment, etc.) A Normal User cannot themselves make a post. The final persona was a System Admin. As you can imagine, there may be some disrespectful comments on a Verified Users Post if their advice doesn't age well. At Sports Bettr we want to protect our experts against this, so System Admins have the ability to enact "discipline" whoch can range from just deleting a comment, to banning/deleting a user.

### Phase 2
During phase 2 we made our ER diagrams as well as our SQL file for our database. 

### Phase 3
During Phase 3 of the project, we generated mock data using Mockaroo and updated the SQL file accordingly, which will be discussed later. We designed two blueprints for distinct user personas: Verified User and System Admin. Our application features multiple pages to represent different screens within the app.

The application begins at the homepage, where users can identify themselves as either an admin or a verified user. Based on their selection, they are directed to the appropriate login page. If the login credentials are valid, they will gain access to their respective dashboard; otherwise, an error message will be displayed.

Upon successful login, users are directed to their dashboard pages. For System Admins, this is the AdminDashboard, which provides an overview of all users, posts, and the ability to add or delete admins. Verified Users, on the other hand, are directed to the MyStuff page, where they can view, create, edit, or delete their posts.

#### Changes from phase 2 to 3 and disclaimers
#### When making Mockaroo data we ran into some small issues, mainly due to Mockaroo not being able to create distinct Strings. Due to this we changed/added some Primary Keys which had to be integrs. This is because we could then use "Row Number" on Mockaroo to guarantee that they would be distinct. Due to this our SQL file was changed a fair amount from Phase 2, which in turn would make our diagram different as well. We hope that this is acceptable because there was no error in the original file, and that if nit using Mock Data, that file would have been able to stand.


## Navigate

### SQL file with Mock data
This can be found at db/SportsBettr.sql

### Blueprints
System Admin Blueprint can be found under src/SystemAdmin/SystemAdmin.py
Verified User Blueprint can be found under src/VerifiedUser/VerifiedUser.py

### ThunderClient Tests
-ThunderClient Tests can be found under thunder-tests/thunderclient.json

### Please refer to docker-compose.yml for code behind setting up the web, db, and appsmith containers


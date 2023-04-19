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





Test push

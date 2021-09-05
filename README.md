# Oxytocin Whatsapp Bot!

Takes care of your personal store using Twilio API with functionalities:
1. Adding Product
2. Changing Product
3. Changing inventory of product
4. View a particularly product
5. View all products on frontend webapp

Technologies used:
**Flask**, **TwilioAPI**, **mongoDB**


# Higher Level Architecture

Consists of three main files:
|File|  Use |
|--|--|
| /app.py | Takes care of API endpoints of flask and also takes care of responding back according to the case
 services/products.py|Contains functions related to CRUD operations on the mongo database
  utils/message.py|Contains all possibilities of responses to be sent


## How to run locally

 Prerequirements:
 

 - ngrok
 - twilio account

Steps to run locally:

 - Set up twilio console and add your number to the whitelist
 - Run    `ngrok http 5000`
 - Put the link starting with https:// into the twilio console 
 - Send "menu" to the twilio number
 

## Steps to run the deployed server

 - Send a **WhatsApp message** to  +1 415 523 8886 with code **join
   wherever-differ**.
   
 - Send "menu" to the same number.

## Frontend Deployement Link

**Frontend webapp to see all the products:** https://oxytocin-bot.herokuapp.com/

## ScreenShots

![ss1](https://i.ibb.co/fSRd6z5/ss1.png)
![ss2](https://i.ibb.co/RcrWR4D/ss2.png)
![ss3](https://i.ibb.co/Z6TLLr6/ss3.png)

## Video Demo Link
to be added

from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse

import services.products as prd
import utils.message as msg
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://aditya:pass123@cluster0.qlbbb.mongodb.net/Oxytocin?retryWrites=true&w=majority"
mongo = PyMongo(app)

products = mongo.db.Products

@app.route('/')
def index():
    saved_products = products.find()
    return render_template('index.html', products = saved_products)


@app.route('/whatsapp', methods=['POST'])
def reply_with_recipe_info():
    message = request.values.get('Body')
    # message = message.lower()

    res = ""
    if message.lower() == "menu":
        res += msg.insert_product_script(0)
        res += "\n"
        res += msg.insert_product_script(1)

    elif message == "A" :
        res += msg.insert_product_script(2)
    elif message == "B":
        res += msg.insert_product_script(7)
    elif message == "C":
        res += msg.insert_product_script(8)
    elif message == "D":
        res += "click on the link: www.oxytocin-bot.herokuapp.com \n"
        print(res)
    elif 'UPI' in message:
        unique_identifier = message.split()[1]
        check = prd.check_for_product(unique_identifier)
        # print(check)
        if check == True:
            res += msg.insert_product_script(3)
        else:
            dic_to_add = {
                'unique_identifier': unique_identifier,
                'product_name' : "Not_Set",
                'Description' : "Not_Set",
                'inventory' : "0"
            }
            prd.insert_product(dic_to_add)
            res += msg.insert_product_script(4)
    elif 'PN' in message:
        message_array = message.split()
        unique_identifier = message_array[1]

        check = prd.check_for_product(unique_identifier)
        if check == False:
            res += "Sorry, your unique identifier wasn't in our database, please look again."
        else:
            product_name = ""

            for i in range(2, len(message_array)):
                # print(i, message_array[i])
                product_name += message_array[i]
                product_name += " "
            
            # print(Description_to_add)
            prd.set_product_name(unique_identifier, product_name)

            res += msg.insert_product_script(5)
    elif 'PD' in message:
        
        message_array = message.split()
        unique_identifier = message_array[1]

        check = prd.check_for_product(unique_identifier)
        if check == False:
            res += "Sorry, your unique identifier wasn't in our database, please look again."
        else:
            Description_to_add = ""

            for i in range(2, len(message_array)):
                # print(i, message_array[i])
                Description_to_add += message_array[i]
                Description_to_add += " "
            
            # print(Description_to_add)
            prd.set_product_description(unique_identifier, Description_to_add)

            res += msg.insert_product_script(6)
    elif 'INV' in message:
        message_array = message.split()
        unique_identifier = message_array[1]

        check = prd.check_for_product(unique_identifier)
        if check == False:
            res += "Sorry, your unique identifier wasn't in our database, please look again."
        else:
            inventory_new = message_array[2]
            prd.change_inventory(unique_identifier, inventory_new)
            res += msg.insert_product_script(-1)
    elif 'VW' in message:
        message_array = message.split()
        unique_identifier = message_array[1]

        check = prd.check_for_product(unique_identifier)
        
        if check == False:
            res += "Sorry, your unique identifier wasn't in our database, please look again."
        else:
            result = prd.view_product(unique_identifier)[0]

            for key, value in result.items():
                if(key == '_id'):
                    continue
                res += key
                res += " : "
                res += value
                res += "\n"
            
            # print(res)
    else:
        res += "Something went wrong. Please look if your message fits in the given format."

    response = MessagingResponse()
    response.message(res)
    # print(message)

    return str(response)


if __name__ == '__main__':
    app.run()
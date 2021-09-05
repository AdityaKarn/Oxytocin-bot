from pymongo import MongoClient


client = MongoClient("mongodb+srv://aditya:pass123@cluster0.qlbbb.mongodb.net/Oxytocin?retryWrites=true&w=majority")
product = client['Oxytocin']['Products']

# db = client.ctox
# serverStatusResult = db.command("serverStatus")
# print(serverStatusResult)


def check_for_product(product_id):

    found_data = product.find({'unique_identifier': product_id})

    result = []
    for data in found_data:
        print("data",data)
        result.append(data)
    
    print(result)
    if len(result) == 0:
        return False
    else:
        return True

def insert_product(dict):
    product.insert_one(dict)

def set_product_name(product_id, product_name):
    product.update({
        'unique_identifier': product_id
        },
        {"$set":
            {'product_name':product_name} 
        }
    )

def set_product_description(product_id, product_description):
    product.update({
        'unique_identifier': product_id
        },
        {"$set":
            {'Description':product_description} 
        }
    )

def change_inventory(product_id, inventory_new):
    product.update({
        'unique_identifier': product_id
        },
        {"$set":
            {'inventory':inventory_new} 
        }
    )

def view_product(product_id):
    result = []
    found_data = product.find({'unique_identifier': product_id})
    for data in found_data:
        result.append(data)
    print(result)
    return result


def insert_product_script(idx):
    scripts = [
        "Send A for adding a product",
        "Send B for viewing product\nSend C for setting inventory \nSendD to view all products",
        "Ok, what is your product's unique identifier? \n Send UPI + <your own unique identifier>",
        "Sorry your unique identifier is already present, please enter any other unique identifier",
        "What's the product name? \n Send PN + <your unique identifier> + <product name>",
        "Done, what is your product's description \n Send PD + <your unique identifier> + <your product description>",
        "Added, do you want to set inventory? \n Send INV + <your unique identifier> + <inventory you want to set>." ,
        "To view a product, send VW + <your unique identifier>",
        "To set Inventory, \n Send INV + <your unique identifier> + <inventory you want to set>"
        "Sorry, your unique identifier wasn't in our database, please look again.",
        "Done."
    ]
    return scripts[idx]

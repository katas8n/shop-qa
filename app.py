# 1) Context menu : a) All products b) Buy product c) Registration d) Auth e) Balance q) Quit
#  product - manufacturer , label , price , date

# Dict -> object
# {
#    "key" : "value"
# }

# a)  All products - print all products into the console
# []

# b) cart -> history of user shopping

# user = { "login" , "password" , "money" , "money_transfer"}
# c)  - register / auth
# q)  - quit
# buy car
# money_transfer

# e) Balance

# b)  Buy product -> if money enough -> buy car -> - money

from datetime import date

def is_exit():
    result = input("Do you wanna quit ? y/n : ")
    return result.lower()

def show_products (list_of_products):
    for product in list_of_products:
        print("\n")
        print("***********************" + product['label'] + "***********************\n")

        for key , value in product.items() :
            if key == "date" : continue
            print(key + " ====> " + value)


products = [
    {
        "manufacturer" : "Czech Republic",
        "label" : "Skoda",
        "price" : "30000 y.e",
        "date" : date(2023,11,1),
        "category" : "sedan"
    },
    {
        "manufacturer": "Italy",
        "label": "Fiat",
        "price": "20000 y.e",
        "date": date(2021, 6, 1),
        "category" : "sedan"
    },
    {
        "manufacturer": "Germany",
        "label": "BMW",
        "price": "10000 y.e",
        "date": date(2002, 8, 1),
        "category" : "crossover"
    },
    {
        "manufacturer": "Germany",
        "label": "MB",
        "price": "20000 y.e",
        "date": date(2012, 12, 2),
        "category" : "sedan"
    },
    {
        "manufacturer": "Germany",
        "label": "VW",
        "price": "10000 y.e",
        "date": date(2011, 12, 2),
        "category" : "truck"
    },
    {
        "manufacturer": "Italy",
        "label": "Alfa Romeo",
        "price": "10000 y.e",
        "date": date(2021, 6, 12),
        "category" : "crossover"
    },
]

is_running = True

is_registred = False

while is_running :
    user_choose = input("""
        a) Show products 
        b) Buy product 
        c) Register
        d) Auth
        e) Balance
        q) Quit
        
    Answer : """).lower()

    if user_choose == "a" :
        show_products(products)

    elif user_choose == "q":
        result = is_exit()

        if result == "y" :
            is_running = False

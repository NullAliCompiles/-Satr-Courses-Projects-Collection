class Bike: #The Bike's class
    #Attribuites:
    def __init__(self, description, cost, sale_price, condition): 
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
#This part is to make the default state for if the Bike is sold or not "False"
        self.sold = False

#Methods:
    def sell(self): #Changes the state of bike.sold to True
        self.sold = True

    def update_sale_price(self, new_sale_price):
        if self.sold: #if the bike has already been sold (bike.sold == True):
            print('Action not allowed, Bike has already been sold')
        else: #If bike.sold == False:
            self.sale_price = new_sale_price


bike1 = Bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
bike1.update_sale_price(350)
bike1.sell()



# The original code in POP:

# def update_sale_price(bike, sale_price):
#     if bike['sold'] == True:
#         print('Action not allowed, Bike has already been sold')
#     else:
#         bike['sale_price'] = sale_price


# def sell(bike):
#     bike['sold'] = True


# def create_bike(description, cost, sale_price, condition):
#     return {
#         'description': description,
#         'cost': cost,
#         'sale_price': sale_price,
#         'condition': condition,
#         'sold': False
#     }


# bike1 = create_bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
# update_sale_price(bike1, 350)
# sell(bike1)

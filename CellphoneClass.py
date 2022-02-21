import random

class Cellphone:
    
# the __init__ metho initializes the attributes.
    def __init__(self, manufacturer,model,retail_price):
        self.__manufact = manufacturer
        self.__model = model
        self. __retail_price = retail_price
        
#the set_manufact method accepts an argument for the phone's manufacturer
#and the rest

    def set_manufact (self,manufacturer):
        self.__manufact = manufacturer

    def set_model  (self, model):
        self.__model = model

    def set_retail_price (self):
        self.__retail_price = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price



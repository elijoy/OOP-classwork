import CellphoneClass as cc

def main():

#variables
    manufacturer =  "Verizon"
    model = "iPhone 10"
    retail_price = "$1000"
    my_cell = cc.Cellphone(manufacturer, model, retail_price)

    
    
    print("Manufacturer is: ", my_cell.get_manufact())
    print("Model is: ", my_cell.get_model())
    print("Retail Price is: ", my_cell.get_retail_price())

    #input functions
    my_cell.set_manufact = input("Enter manufacturer: ")
    my_cell.set_model = input("Enter model: ")
    my_cell.set_retail_price = float(input("Enter retail price: "))

    print("Manufacturer is: ", my_cell.get_manufact())
    print("Model is: ", my_cell.get_model())
    print("Retail Price is: ", my_cell.get_retail_price())



    

main()
import InsectClass as i

def main():
    mosquito = i.Insect(2,4)
    housefly = i.Insect(3,6)

    mosquito.flight_length()
    housefly.flight_length()



    print("The mosquito can fly this many miles: ", mosquito.get_miles())
    print("The housefly can fly this many miles: ", mosquito.get_miles())

main()

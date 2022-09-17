# Design a food menu app where a user can select an item out of multiple 
# choices shown to the user. The item selected by the user is shown to the user as the output.

if __name__ == "__main__":
    menu = ['1_pizza', '2_pasta', '3_Carpaccio', '4_Risotto']
    print (menu)
    dish = int(input("Please select item number from the menu :"))
    print (menu[dish - 1])

    
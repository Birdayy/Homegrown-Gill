# My task is to create a program that allows the user to order food from the seller
# It is supposed to show which food the user can order, once they order show the price and what they ordered.


def printoptions(mylisttoworkwith):
    for item in mylisttoworkwith:
        print(mylisttoworkwith.index(item)+1, item)


def validate(question, minimum, maximum):
    loop = True

    while loop:
        try:
            choice = int(input(question))
            # should check if the input is between min and max
            if choice > minimum and choice < maximum:
                return choice

            else:
                choice = int(input(question))

            #return choice   # choice is valid
        except ValueError:
            choice = int(input(question))




def dealwithfruits(cartlist, cartpricelist):
    # display list of fruits
    listoffruits = ["Apples", "Bananas", "Oranges", "Plums", "Back"]
    printoptions(listoffruits)
    while True:
        fruits_choice = input("Which fruit would you like? ")

        if fruits_choice == "1":
            quantity_apples = validate("How many would you like? $4.00(per 1kg -- 1kg minimum)", 0, 100)
            # print('quantity apples is {}'.format(quantity_apples))
            apple_cost = int(quantity_apples) * 4
            print("{}kg(s) of apples have been added to your order.".format(quantity_apples))
            print("This will cost ${}".format(apple_cost))

            cartlist.append('Apples')
            cartpricelist.append(apple_cost)
            return cartlist, cartpricelist

        if fruits_choice == "2":
            quantity_bananas = validate("How many would you like? $3.00(per 1kg -- 1kg minimum)", 0, 100)
            banana_cost = int(quantity_bananas) * 3
            print("{}kg(s) of bannanas have been added to your order.".format(quantity_bananas))
            print("This will cost ${}".format(banana_cost))

            cartlist.append('Bananas')
            cartpricelist.append(banana_cost)
            return cartlist, cartpricelist

        if fruits_choice == "3":
            quantity_oranges = validate("How many would you like? $3.50(per 1kg -- 1kg minimum)", 0, 100)
            orange_cost = int(quantity_oranges) * 3.50
            print("{}kg(s) of oranges have been added to your order.".format(quantity_oranges))
            print("This will cost ${}".format(orange_cost))

            cartlist.append('Oranges')
            cartpricelist.append(orange_cost)
            return cartlist, cartpricelist

        if fruits_choice == "4":
            quantity_plums = validate("How many would you like? $8(per 1kg -- 1kg minimum)", 0, 100)
            plum_cost = int(quantity_plums) * 8
            print("{}kg(s) of plums have been added to your order.".format(quantity_plums))
            print("This will cost ${}".format(plum_cost))

            cartlist.append('Plums')
            cartpricelist.append(plum_cost)
            return cartlist, cartpricelist

        if fruits_choice == "5":
            break

        break
    # allow the user to choose
    # need input again
    # loop through the choices of fruit
    # update some sort of cart - build a list of chosen items with cost
    # update totalcost
    # output final order at the end

    # show the cart can be a function
    # def showcart(orderlist) printorderlist (yourlatestcartlist)


def dealwithvegetables(cartlist, cartpricelist):
    listofvegetables = ["Carrots", "Lettuce", "Potatoes", "Pumpkins", "Back"]
    printoptions(listofvegetables)
    while True:
        vegetable_choice = input("Which vegetable would you like? ")
        if vegetable_choice == "1":
            quantity_carrots = validate("How many would you like? $2.00(per 1kg -- 1kg minimum)", 0, 100)
            carrot_cost = int(quantity_carrots) * 2
            print("{}kg(s) of carrots have been added to your order.".format(quantity_carrots))
            print("This will cost ${}".format(carrot_cost))

            cartlist.append('Carrots')
            cartpricelist.append(carrot_cost)
            return cartlist, cartpricelist

        if vegetable_choice == "2":
            quantity_lettuce = validate("How many would you like? $3.50(each)", 0, 100)
            lettuce_cost = int(quantity_lettuce) * 3.50
            print("{}(s) lettuces have been added to your order.".format(quantity_lettuce))
            print("This will cost ${}".format(lettuce_cost))

            cartlist.append('Lettuce')
            cartpricelist.append(lettuce_cost)
            return cartlist, cartpricelist

        if vegetable_choice == "3":
            quantity_potatoes = validate("How many would you like? $2.50(per 1kg -- 1kg minimum)", 0, 100)
            potato_cost = int(quantity_potatoes) * 2.50
            print("{}kg(s) of potatoes have been added to your order.".format(quantity_potatoes))
            print("This will cost ${}".format(potato_cost))

            cartlist.append('Potatoes')
            cartpricelist.append(potato_cost)
            return cartlist, cartpricelist

        if vegetable_choice == "4":
            quantity_pumpkins = validate("How many would you like? $5.00(each)", 0, 100)
            pumpkin_cost = int(quantity_pumpkins) * 5
            print("{}(s) pumpkins have been added to your order.".format(quantity_pumpkins))
            print("This will cost ${}".format(pumpkin_cost))

            cartlist.append('Pumpkin')
            cartpricelist.append(pumpkin_cost)
            return cartlist, cartpricelist

        if vegetable_choice == "5":
            break


def dealwithdairy(cartlist, cartpricelist):
    listofdairy = ["Milk", "Butter", "Cream", "Back"]
    printoptions(listofdairy)

    while True:
        diary_choice = input("Which diary product would you like? ")

        if diary_choice == "1":
            quantity_milk = validate("How much would you like? $2.50(per 1L -- 1L minimum)", 0, 100)
            milk_cost = int(quantity_milk) * 2.50
            print("{}L(s) of milk has been added to your order.".format(quantity_milk))
            print("This will cost ${}".format(milk_cost))

            cartlist.append('Milk')
            cartpricelist.append(milk_cost)
            return cartlist, cartpricelist

        if diary_choice == "2":
            quantity_butter = validate("How many would you like? $6(each)", 0, 100)
            butter_cost = int(quantity_butter) * 6
            print("{} butters have been added to your order.".format(quantity_butter))
            print("This will cost ${}".format(butter_cost))

            cartlist.append('Butter')
            cartpricelist.append(butter_cost)
            return cartlist, cartpricelist

        if diary_choice == "3":
            quantity_cream = validate("How much would you like? $3.50(each)", 0, 100)
            cream_cost = int(quantity_cream) * 3.50
            print("{} bottles of cream have been added to your order.".format(quantity_cream))
            print("This will cost ${}".format(cream_cost))

            cartlist.append('Cream')
            cartpricelist.append(cream_cost)
            return cartlist, cartpricelist

        if diary_choice == "4":
            break


def dealwithnuts(cartlist, cartpricelist):
    listofnuts = ["Almonds", "Cashews", "Walnuts", "Back"]
    printoptions(listofnuts)

    while True:
        nut_choice = input("Which type of nut would you like? ")

        if nut_choice == "1":
            quantity_almonds = validate("How much would you like? $4.00(per 100g -- 100g minimum)", 0, 100)
            almond_cost = int(quantity_almonds) * 4
            print("{}g(s) of almonds have been added to your order.".format(quantity_almonds))
            print("This will cost ${}".format(almond_cost))

            cartlist.append('Almonds')
            cartpricelist.append(almond_cost)
            return cartlist, cartpricelist

        if nut_choice == "2":
            quantity_cashews = validate("How much would you like? $3.00(per 100g -- 100g minimum)", 0, 100)
            cashew_cost = int(quantity_cashews) * 3
            print("{}g(s) of cashews have been added to your order.".format(quantity_cashews))
            print("This will cost ${}".format(cashew_cost))

            cartlist.append('Cashews')
            cartpricelist.append(cashew_cost)
            return cartlist, cartpricelist

        if nut_choice == "3":
            quantity_walnuts = validate("How much would you like? $2.50(per 100g -- 100g minimum)", 0, 100)
            walnut_cost = int(quantity_walnuts) * 2.50
            print("{}g(s) of walnuts have been added to your order.".format(quantity_walnuts))
            print("This will cost ${}".format(walnut_cost))

            cartlist.append('Walnuts')
            cartpricelist.append(walnut_cost)
            return cartlist, cartpricelist

        if nut_choice == "4":
            break


def dealwithjams(cartlist, cartpricelist):
    listofjams = ["Strawberry", "Apricott", "Raspberry", "Back"]
    printoptions(listofjams)

    while True:
        jam_choice = input("Which type of jam would you like? ")

        if jam_choice == "1":
            quantity_strawberry_jam = validate("How many would you like? $2.50(each)", 0, 100)
            strawberry_jam_cost = int(quantity_strawberry_jam) * 2.50
            print("{} strawberry jams have been added to your order.".format(quantity_strawberry_jam))
            print("This will cost ${}".format(strawberry_jam_cost))

            cartlist.append('Strawberry Jam')
            cartpricelist.append(strawberry_jam_cost)
            return cartlist, cartpricelist

        if jam_choice == "2":
            quantity_apricott_jam = validate("How many would you like? $2.50(each)", 0, 100)
            apricott_jam_cost = int(quantity_apricott_jam) * 2.50
            print("{} apricott jams have been added to your order.".format(quantity_apricott_jam))
            print("This will cost ${}".format(apricott_jam_cost))

            cartlist.append('Apricott Jam')
            cartpricelist.append(apricott_jam_cost)
            return cartlist, cartpricelist

        if jam_choice == "3":
            quantity_raspberry_jam = validate("How many would you like? $2.50(each)", 0, 100)
            raspberry_jam_cost = int(quantity_raspberry_jam) * 2.50
            print("{} raspberry jams have been added to your order.".format(quantity_raspberry_jam))
            print("This will cost ${}".format(raspberry_jam_cost))

            cartlist.append('Raspberry Jam')
            cartpricelist.append(raspberry_jam_cost)
            return cartlist, cartpricelist

        if jam_choice == "4":
            break


def dealwithjuices(cartlist, cartpricelist):
    listofjucies = ["Orange Juice", "Apple Juice", "Cranberry Juice", "Back"]
    printoptions(listofjucies)

    while True:
        juice_choice = input("Which type of juice would you like? ")

        if juice_choice == "1":
            quantity_orange_juice = validate("How much would you like? $2(per L -- 1L minimum)", 0, 100)
            orange_juice_cost = int(quantity_orange_juice) * 2.50
            print("{}L(s) of orange juice has been added to your order.".format(quantity_orange_juice))
            print("This will cost ${}".format(orange_juice_cost))

            cartlist.append('Orange Juice')
            cartpricelist.append(orange_juice_cost)
            return cartlist, cartpricelist

        if juice_choice == "2":
            quantity_apple_juice = validate("How much would you like? $1(per L -- 1L minimum)", 0, 100)
            apple_juice_cost = int(quantity_apple_juice) * 2.50
            print("{}L(s) of apple juice has been added to your order.".format(quantity_apple_juice))
            print("This will cost ${}".format(apple_juice_cost))

            cartlist.append('Apple Juice')
            cartpricelist.append(apple_juice_cost)
            return cartlist, cartpricelist

        if juice_choice == "3":
            quantity_cranberry_juice = validate("How much would you like? $2(per L -- 1L minimum)", 0, 100)
            cranberry_juice_cost = int(quantity_cranberry_juice) * 2.50
            print("{}L(s) of cranberry juice has been added to your order.".format(quantity_cranberry_juice))
            print("This will cost ${}".format(cranberry_juice_cost))

            cartlist.append('Cranberry Juice')
            cartpricelist.append(cranberry_juice_cost)
            return cartlist, cartpricelist

        if juice_choice == "4":
            break


print("Welcome to Homegrown Gill's click and collect!")

loop = True
while loop:
    order_type = input("Pick up(1) or Delivery(2)? (select 1 or 2) ")
    # this variable is to find out whether I need to ask the user their name, address etc or not
    # I made the 1 or 2 to make it easier for the user
    if order_type == "1":

        while True:
            # User inputs their name
            name = input("What is your name? ")
            # The name variable can only be 100 characters long
            if len(name) <= 100:
                break

            else:
                # If the user enters more than 100 characters
                print("Too many characters")
                print("Please try again")
        if name.isalpha():
            # If the name is letters
            # Makes the name lower case, then takes away any extra spaces then makes the first letter uppercase
            print("Hello {}!".format(name).lower().strip().title())

        loop = False

    elif order_type == "2":
        name = input("What is your name?")
        address = input("What is the delivery address?")
        while True:
            box_or_bag = input("Would you like your food to be delivered in a box (1) or a bag (2) ")
            if box_or_bag == "1":
                print("You have selected a box.")
                break
            if box_or_bag == "2":
                print("You have selected a bag.")

                break
            else:
                print("Please enter a valid input")
        loop = False
    else:
        print("Please enter a valid answer")


def dealwithfoodchoices(numberchoice, cart, carttotal):
    if numberchoice is 1:
        # print(cart, carttotal)
        # print('your order so far is >>')
        # printoptions(cart)
        # printoptions(carttotal)
        print(dealwithfruits(cart, carttotal))
        return cart, carttotal

    elif numberchoice is 2:
        # print(cart, carttotal)
        print(dealwithvegetables(cart, carttotal))
        return cart, carttotal

    elif numberchoice is 3:
        # print(cart, carttotal)
        print(dealwithdairy(cart, carttotal))
        return cart, carttotal

    elif numberchoice is 4:
        # print(cart, carttotal)
        print(dealwithnuts(cart, carttotal))
        return cart, carttotal

    elif numberchoice is 5:
        # print(cart, carttotal)
        print(dealwithjams(cart, carttotal))
        return cart, carttotal

    elif numberchoice is 6:
        # print(cart, carttotal)
        print(dealwithjuices(cart, carttotal))
        return cart, carttotal

    elif numberchoice is 7:
        print(cart)
        print("Your order will cost ${}".format(totalcost))
        print("Thank you for shopping with us.")
    # update cart
    # update total
    return cart, carttotal


cartorder = []  # build your order here
cartprices = []  # build your total price
totalcost = 0
loop = True

while loop:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    food_types = ["Fruits", "Vegetables", "Dairy", "Nuts", "Jams", "Juices", "Checkout"]

    printoptions(food_types)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    food_type = input("What type of food would you like? Choose a number from the options above ")

    if food_type == "7":
        print(cartorder)
        print("Your order will cost ${}".format(totalcost))
        print("Thank you for shopping with us.")
        break

    # print ('this is food_type: {} and the type is {}'.format(food_type, type(food_type)))
    for i in range(len(food_types)):
        if food_type == str((i+1)):
            # call the function that deals with fruit
            # dealwithfruits()
            cartorder, cartprices = dealwithfoodchoices(i+1, cartorder, cartprices)
            # print(cartorder)
            # print(cartprices)

    printoptions(cartorder)
    # printoptions(cartprices)
    # sum all of the prices to find final price
    if food_type > "0" and food_type < "8":
        for i in range(len(cartprices)):
            totalcost += cartprices[i]

    print("Your order so far costs ${}".format(totalcost))

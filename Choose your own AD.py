name = input("You name:")
print("Welcome", name,'To this adventure!')

answer = input(
    "You are on a dirt road, it has come to an end and you go left or right.Which way would you like to go: ").lower()
if answer == "left":
    answer = input("You come to river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()
    if answer == "swim":
        print("You swam acrross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game ")
    else:
        print('Not a valid option. you lose')

elif answer == "right":
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it ot head back? (cross/back): ').lower()

    if answer == "back":
        print("you go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger.Do you talk to them(yes/no): ").lower()
        if answer == "yes":
            print("You talk to the starnger and they give you gold. You WIN")
        elif answer == "no":
            print('You ignore the stranger and the are offended and you lose')
        else:   
             print('Not a valid option. you lose')
    else:
            print('Not a valid option. you lose')
else:
        print('Thank you for trying.', name)

